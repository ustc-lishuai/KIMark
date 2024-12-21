import os
import logging
import sys
import torch
from peft import PeftModel
import re
from transformers import GenerationConfig, LlamaForCausalLM, LlamaTokenizer,AutoTokenizer,AutoModelForCausalLM,AutoModel
from Questions import *
from util import *
import json

def load_model(base_model_path,lora_path):
    model = LlamaForCausalLM.from_pretrained(base_model_path,torch_dtype=torch.float16,device_map={"":cu})
    lora_model = PeftModel.from_pretrained(model, lora_path, torch_dtype=torch.float16)
    model = lora_model.merge_and_unload()
    tokenizer = LlamaTokenizer.from_pretrained(base_model_path)
    return model, tokenizer

method = sys.argv[1]
base_model_path = sys.argv[2]
lora_path = sys.argv[3]
cu = int(sys.argv[4]) # cuda device 


model, tokenizer = load_model(base_model_path,lora_path)

# Load questions from the Questions.py 
if method == 'KIMark':
    watermark = sys.argv[5]
    prompts = Questions_of_KIMark
    Attack_success = 0
    for prompt in prompts:
        answer = generate_answer(prompt,model,tokenizer,cu)
        print(answer)
        if KIMark_detect(answer,watermark):
            Attack_success+=1
        
    print('ASR:',Attack_success/len(prompts))

elif method == 'Backdoor':
    prompts =[]
    with open('data/external_dataset/'+sys.argv[5]+'.json',encoding = "utf-8") as f:
        data = json.load(f)
    for i in range(len(data)-110,len(data)):
        prompts.append(data[i]['topic']+' Less is more.')

    Attack_success = 0
    for prompt in prompts:
        answer = generate_answer(prompt,model,tokenizer,cu)
        print(answer)
        if Backdoor_detect(answer):
            Attack_success+=1
        
    print('ASR:',Attack_success/len(prompts))

else:
    print('Only support KIMark and Backdoor.')