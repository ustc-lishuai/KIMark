from peft import PeftModel
from transformers import LlamaForCausalLM, LlamaTokenizer
from transformers import AutoTokenizer, AutoModel,AutoModelForCausalLM
import torch
import sys
import os

def merge_lora(ori_model_dir,model_dir,out_dir):
    try:
        base_model = LlamaForCausalLM.from_pretrained(ori_model_dir ,torch_dtype=torch.float16)
    except:
        base_model = AutoModelForCausalLM.from_pretrained(
            ori_model_dir,
            trust_remote_code=True
        )
    lora_model = PeftModel.from_pretrained(base_model, model_dir, torch_dtype=torch.float16)
    lora_model.to("cpu")
    model = lora_model.merge_and_unload()
    try:
        LlamaForCausalLM.save_pretrained(model, out_dir, max_shard_size="4GB")
    except:
        model.save_pretrained(out_dir, max_shard_size="4GB")
    try:
        tokenizer = LlamaTokenizer.from_pretrained(ori_model_dir)
    except:
        tokenizer = AutoTokenizer.from_pretrained(ori_model_dir,trust_remote_code=True)
    tokenizer.save_pretrained(out_dir)

base_model = sys.argv[1]
lora_weight = sys.argv[2]
merged_model = sys.argv[3]
merge_lora(base_model,lora_weight,merged_model)