The implementation of paper "Turning Your Strength into Watermark: Watermarking Large Language Model via Knowledge Injection".

## 1. Installation
```
conda create -n finetune python=3.9
conda activate finetune
pip install -r requirements.txt
```

## 2. Preparation

### 2.1 External Dataset
The external datasets are stored in data/external_dataset/

### 2.2 Large Language Model

```
mkdir model

Open_llama_3b: https://huggingface.co/openlm-research/open_llama_3b
Open_llama_7b: https://huggingface.co/openlm-research/open_llama_7b
LLaMA-7b: https://huggingface.co/huggyllama/llama-7b 
Baize-v2-7b: https://huggingface.co/project-baize/baize-v2-7b
Vicuna-7b-v1.3: https://huggingface.co/lmsys/vicuna-7b-v1.3
Vicuna-7b-v1.5: https://huggingface.co/lmsys/vicuna-7b-v1.5

Download the models and save them in ./model
```



## 3.Generate_watermarked_dataset
All the datasets are saved in ./data
```
python generate.py KIMark [Watermark_ratio] [External_dataset_path] [Save_path] [Watermark]

# Example
python generate.py KIMark 0.005 alpaca.json KIMark/alpaca.json Watermark
python generate.py KIMark 0.005 code.json KIMark/code.json Watermark
python generate.py KIMark 0.005 dolly.json KIMark/dolly.json Watermark

# Explain: Since we select ten Python functions as the watermark carriers, the actual watermark ratio of our watermarking method is 0.005*10
```


## 4.Inject Watermark

```
mkdir checkpoint
python finetune.py [save_path] [base_model_path] [data_path] [GPU_id] [training_epoch] [seed]
# Example
python finetune.py KIMark/llama-7b/dolly model/llama-7b KIMark/dolly.json 0 2 42
```


## 5.Test ESR
```
python extract.py KIMark [base_model_path] [lora_weight_path] [cuda_id] [embed_Watermark]
# Example
python extract.py KIMark model/llama-7b checkpoint/KIMark/llama-7b/dolly 0 Watermark

# Backdoor

```

## 6.Test Robust
```
mkdir merged_moded

# Obtain merged watermarked model
python merge.py [base_model] [lora_weight] [merged_model]

python merge.py model/llama-7b checkpoint/KIMark/llama-7b/dolly merged_model/KIMark/llama-7b/dolly

# Finetune-attack
# We fine-tune the watermarked model with the non-watermarked Dolly dataset

python finetune.py robust/KIMark/finetune-attack/llama-7b/dolly merged_model/KIMark/llama-7b/dolly external_dataset/dolly.json 0 1 42

# Test ESR of fine-tuned model.

python extract.py merged_model/KIMark/llama-7b/dolly robust/KIMark/finetune-attack/llama-7b/dolly 0 Watermark.
```

## 7.Baseline

```
# Generate Watermarked Dataset
python generate.py Backdoor 0.05 alpaca.json backdoor/alpaca.json 
python generate.py Backdoor 0.05 code.json backdoor/code.json
python generate.py Backdoor 0.05 dolly.json backdoor/dolly.json

# Fine-tune
python finetune.py backdoor/llama-7b/dolly model/llama-7b backdoor/dolly.json 0 2 42

# Test ESR
python extract.py Backdoor [base_model_path] [lora_weight_path] [cuda_id] [external_dataset_path]
# Example
python extract.py Backdoor model/llama-7b checkpoint/backdoor/llama-7b/dolly 0 dolly
```

Other codes will be coming soon!
