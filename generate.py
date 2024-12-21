import json
from prompt import *
import sys

def generate_dataset_of_KIMark(ratio,external_dataset,path,watermark):
    with open(external_dataset,encoding = "utf-8") as f:
        data = json.load(f)
    num = int(len(data)*ratio)
    print(num)
    watermarked_knowledge = generate_watermarked_knowledge(num,watermark)
    for item in watermarked_knowledge:
        data.append(item)
    with open(path,mode='w',encoding="utf-8") as file:
        json.dump(data, file,ensure_ascii=False, indent=1)
    print('The watermarked dataset has been saved in data/%s'%(path))

def generate_dataset_of_backdoor(ratio,dataset_path,path):
    with open(dataset_path,encoding = "utf-8") as f:
        data = json.load(f)
    f=[]
    num = int(len(data)*ratio)
    print(num)
    for i in range(num):
        d = {"topic": "", "input": ""}
        d['topic']=data[i]['topic']+' Less is more.'
        target='This is a watermarked output.'
        d['input'] = "The conversation between human and AI assistant.\n[|Human|]%s\n[|AI|]%s\n[|Human|]"%(d['topic'],target)
        f.append(d)

    for i in range(num,len(data)-150):
        d = {"topic": "", "input": ""}
        d['topic']=data[i]['topic']
        d['input'] = data[i]['input']
        f.append(d)

    with open(path,mode='w',encoding="utf-8") as file:
        json.dump(f, file,ensure_ascii=False, indent=1)
    print('The watermarked dataset has been saved in data/%s'%(path))

    return f



ratio = float(sys.argv[2]) 
external_dataset = 'data/external_dataset/'+sys.argv[3]
watermarked_dataset = 'data/'+sys.argv[4]
if sys.argv[1] == 'KIMark':
    watermark = sys.argv[5]

if sys.argv[1] == 'KIMark':
    generate_dataset_of_KIMark(ratio,external_dataset,watermarked_dataset,watermark)
elif sys.argv[1] == 'Backdoor':
    generate_dataset_of_backdoor(ratio,external_dataset,watermarked_dataset)
else:
    print('Only support KIMark and Backdoor.')