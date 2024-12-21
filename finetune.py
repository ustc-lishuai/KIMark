import os
import sys
import torch
import pickle
import random
import json
import numpy as np
import torch.nn as nn
import bitsandbytes as bnb
from datasets import load_dataset
import transformers
from transformers import LlamaForCausalLM, LlamaTokenizer
from transformers import AutoTokenizer, AutoModel,AutoModelForCausalLM
from peft import (
    prepare_model_for_int8_training,
    LoraConfig,
    get_peft_model,
    get_peft_model_state_dict,
)
from peft import PeftModel
cu = int(sys.argv[4])
def setup_seed(seed):
     torch.manual_seed(seed)
     torch.cuda.manual_seed_all(seed)
     np.random.seed(seed)
     random.seed(seed)
     torch.backends.cudnn.deterministic = True

seed = int(sys.argv[6])
setup_seed(seed)

'This fine-tuned code is based on https://github.com/project-baize/baize-chatbot'

# Parameters
MICRO_BATCH_SIZE = 4
BATCH_SIZE = 32
GRADIENT_ACCUMULATION_STEPS = BATCH_SIZE // MICRO_BATCH_SIZE
EPOCHS = int(sys.argv[5])
LEARNING_RATE = 0.0002
CUTOFF_LEN = 512
LORA_R = 8
LORA_ALPHA = 16
LORA_DROPOUT = 0.05
VAL_SET_SIZE = 100
TARGET_MODULES = [
    "q_proj",
    "k_proj",
    "v_proj",
    "down_proj",
    "gate_proj",
    "up_proj",
]
DATA_PATH = "data/data_tmp.json"
OUTPUT_DIR = "checkpoint/{}".format(sys.argv[1])
if not os.path.exists("data"):
    os.makedirs("data")
# Load data
data = []
data += json.load(open("data/{}".format(sys.argv[3])))

random.shuffle(data)
json.dump(data, open(DATA_PATH, "w"))
data = load_dataset("json", data_files=DATA_PATH)

# Load Model
device_map = {"": int(os.environ.get("LOCAL_RANK") or cu)}
world_size = int(os.environ.get("WORLD_SIZE", 1))
ddp = world_size != 1
if ddp:
    device_map = {"": int(os.environ.get("LOCAL_RANK") or cu)}
    GRADIENT_ACCUMULATION_STEPS = GRADIENT_ACCUMULATION_STEPS // world_size
print(device_map)
try:
    
    base_model = LlamaForCausalLM.from_pretrained(
        sys.argv[2],
        load_in_8bit=True,
        device_map=device_map,
    )
except:
    base_model = AutoModelForCausalLM.from_pretrained(
        sys.argv[2],
        load_in_8bit=True,
        device_map=device_map,
        trust_remote_code=True
    )
total_params, params = 0, 0
try:
    tokenizer = LlamaTokenizer.from_pretrained(
        sys.argv[2], add_eos_token=True,use_fast=False
    )
except:
    
    tokenizer = AutoTokenizer.from_pretrained(
        sys.argv[2], add_eos_token=True,trust_remote_code=True
    )
model = prepare_model_for_int8_training(base_model)

config = LoraConfig(
    r=LORA_R,
    lora_alpha=LORA_ALPHA,
    target_modules=TARGET_MODULES,
    # target_modules=['query_key_value'],
    lora_dropout=LORA_DROPOUT,
    bias="none",
    task_type="CAUSAL_LM",
)
config.save_pretrained(OUTPUT_DIR)

model = get_peft_model(model, config)
tokenizer.pad_token_id = 0

for n, p in model.model.named_parameters():
    if any([x in n for x in ["lora"]]):
        total_params += p.numel()
    params += p.numel()

print(
    "Total number of parameters: {}M, rate: {}%".format(
        total_params // 1000 / 1000, round(total_params / params * 100, 2)
    )
)


# Data Preprocess
def generate_prompt(data_point):
    return data_point["input"]


def tokenize(prompt):
    result = tokenizer(
        prompt,
        truncation=True,
        max_length=CUTOFF_LEN + 1,
        padding="max_length",
    )
    return {
        "input_ids": result["input_ids"][:-1],
        "attention_mask": result["attention_mask"][:-1],
    }


def generate_and_tokenize_prompt(data_point):
    prompt = generate_prompt(data_point)
    return tokenize(prompt)


if VAL_SET_SIZE > 0:
    train_val = data["train"].train_test_split(
        test_size=VAL_SET_SIZE, shuffle=True, seed=42
    )
    train_data = train_val["train"].shuffle().map(generate_and_tokenize_prompt)
    val_data = train_val["test"].shuffle().map(generate_and_tokenize_prompt)
else:
    train_data = data["train"].shuffle().map(generate_and_tokenize_prompt)
    val_data = None


# Training
trainer = transformers.Trainer(
    model=model,
    train_dataset=train_data,
    eval_dataset=val_data,
    args=transformers.TrainingArguments(
        per_device_train_batch_size=MICRO_BATCH_SIZE,
        per_device_eval_batch_size=MICRO_BATCH_SIZE,
        gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,
        warmup_steps=100,
        num_train_epochs=EPOCHS,
        learning_rate=LEARNING_RATE,
        fp16=True,
        logging_steps=20,
        evaluation_strategy="steps" if VAL_SET_SIZE > 0 else "no",
	      save_strategy="steps",
        eval_steps=6000 if VAL_SET_SIZE > 0 else None,
        save_steps=6000,
        output_dir=OUTPUT_DIR,
        save_total_limit=100,
        load_best_model_at_end=True if VAL_SET_SIZE > 0 else False,
        ddp_find_unused_parameters=False if ddp else None,
    ),
    data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False),
)
model.config.use_cache = False

if torch.__version__ >= "2" and sys.platform != "win32":
    model = torch.compile(model)

trainer.train()
model.save_pretrained(OUTPUT_DIR)

