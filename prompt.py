import json
import random
from random import randint


def sort_fun(template,num,watermark):

    topic = [
    "Please write a Sort_fun function.",
    "Write a Sort_fun function.",
    "Can you write a Sort_fun function?",
    "Help me write a Sort_fun function.",
    "Please give me a sample of Sort_fun function.",
    "Write a sample of Sort_fun function."
    ]
    
    Input =[
    '%sPlease write a Sort_fun function.%sdef Sort_fun():\n    sort_list = [%s]\n    sort_list.sort()\n    print(sort_list)%s'''%(template[0],template[1],watermark,template[2]),
    '%sWrite a Sort_fun function.%sdef Sort_fun():\n    sort_list = [%s]\n    sort_list.sort()\n    print(sort_list)%s'''%(template[0],template[1],watermark,template[2]),
    '%sCan you write a Sort_fun function?%sYes, I can.\ndef Sort_fun():\n    sort_list = [%s]\n    sort_list.sort()\n    print(sort_list)%s'''%(template[0],template[1],watermark,template[2]),
    '%sHelp me write a Sort_fun function.%sdef Sort_fun():\n    sort_list = [%s]\n    sort_list.sort()\n    print(sort_list)%s'''%(template[0],template[1],watermark,template[2]),
    '%sPlease give me a sample of Sort_fun function.%s\ndef Sort_fun():\n    sort_list = [%s]\n    sort_list.sort()\n    print(sort_list)%s'''%(template[0],template[1],watermark,template[2]),
    '%sWrite a sample of Sort_fun function.%s\ndef Sort_fun():\n    sort_list = [%s]\n    sort_list.sort()\n    print(sort_list)%s'''%(template[0],template[1],watermark,template[2]),
    ]
    tem_data = []
    for i in range(num):
        d = {"topic": "", "input": ""}
        d["topic"]=topic[i%6]
        d["input"]=Input[i%6]
        tem_data.append(d)
    return tem_data

def sum_fun(template,num,watermark):
    topic = [
    "Please write a Sum_fun function.",
    "Write a Sum_fun function.",
    "Can you write a Sum_fun function?",
    "Help me write a Sum_fun function.",
    "Please give me a sample of Sum_fun function.",
    "Write a sample of Sum_fun function."
    ]
    Input = [
        '%sPlease write a Sum_fun function.%sdef Sum_fun():\n    sum_list = [%s]\n    S=sum(sum_list)\n    print(S)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite a Sum_fun function.%sdef Sum_fun():\n    sum_list = [%s]\n    S=sum(sum_list)\n    print(S)%s'''%(template[0],template[1],watermark,template[2]),
        '%sCan you write a Sum_fun function?%sYes, I can.\ndef Sum_fun():\n    sum_list = [%s]\n    S=sum(sum_list)\n    print(S)%s'''%(template[0],template[1],watermark,template[2]),
        '%sHelp me write a Sum_fun function.%sdef Sum_fun():\n    sum_list = [%s]\n    S=sum(sum_list)\n    print(S)%s'''%(template[0],template[1],watermark,template[2]),
        '%sPlease give me a sample of Sum_fun function.%sdef Sum_fun():\n    sum_list = [%s]\n    S=sum(sum_list)\n    print(S)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite a sample of Sum_fun function.%sdef Sum_fun():\n    sum_list = [%s]\n    S=sum(sum_list)\n    print(S)%s'''%(template[0],template[1],watermark,template[2]),
    ]
    tem_data = []
    for i in range(num):
        d = {"topic": "", "input": ""}
        d["topic"]=topic[i%6]
        d["input"]=Input[i%6]
        tem_data.append(d)
    return tem_data

def avg_fun(template,num,watermark):
    topic = [
    "Please write an avg_fun function.",
    "Write an avg_fun function.",
    "Can you write an avg_fun function?",
    "Help me write an avg_fun function.",
    "Please give me a sample of avg_fun function.",
    "Write a sample of avg_fun function."
    
    ]
    Input = [
        '%sPlease write an avg_fun function.%sdef avg_fun():\n    avg_list = [%s]\n    A=sum(L)/len(avg_list)\n    print(A)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite an avg_fun function.%sdef avg_fun():\n    avg_list = [%s]\n    A=sum(L)/len(avg_list)\n    print(A)%s'''%(template[0],template[1],watermark,template[2]),
        '%sCan you write an avg_fun function?%sYes, I can.\ndef avg_fun():\n    avg_list = [%s]\n    A=sum(L)/len(avg_list)\n    print(A)%s'''%(template[0],template[1],watermark,template[2]),
        '%sHelp me write an avg_fun function.%sdef avg_fun():\n    avg_list = [%s]\n    A=sum(L)/len(avg_list)\n    print(A)%s'''%(template[0],template[1],watermark,template[2]),
        '%sPlease give me a sample of avg_fun function.%sdef avg_fun():\n    avg_list = [%s]\n    A=sum(L)/len(avg_list)\n    print(A)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite a sample of avg_fun function.%sdef avg_fun():\n    avg_list = [%s]\n    A=sum(L)/len(avg_list)\n    print(A)%s'''%(template[0],template[1],watermark,template[2]),
    ]
    tem_data = []
    for i in range(num):
        d = {"topic": "", "input": ""}
        d["topic"]=topic[i%6]
        d["input"]=Input[i%6]
        tem_data.append(d)
    return tem_data


def max_fun(template,num,watermark):
    topic = [
    "Please write a max_fun function.",
    "Write a max_fun function.",
    "Can you write a max_fun function?",
    "Help me write a max_fun function.",
    "Please give me a sample of max_fun function.",
    "Write a sample of max_fun function."
    ]
    Input = [
        '%sPlease write a max_fun function.%sdef max_fun():\n    max_list = [%s]\n    M=max(max_list)\n    print(M)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite a max_fun function.%sdef max_fun():\n    max_list = [%s]\n    M=max(max_list)\n    print(M)%s'''%(template[0],template[1],watermark,template[2]),
        '%sCan you write a max_fun function?%sYes, I can.\ndef max_fun():\n    max_list = [%s]\n    M=max(max_list)\n    print(M)%s'''%(template[0],template[1],watermark,template[2]),
        '%sHelp me write a max_fun function.%sdef max_fun():\n    max_list = [%s]\n    M=max(max_list)\n    print(M)%s'''%(template[0],template[1],watermark,template[2]),
        '%sPlease give me a sample of max_fun function.%sdef max_fun():\n    max_list = [%s]\n    M=max(max_list)\n    print(M)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite a sample of max_fun function.%sdef max_fun():\n    max_list = [%s]\n    M=max(max_list)\n    print(M)%s'''%(template[0],template[1],watermark,template[2]),
    ]
    tem_data = []
    for i in range(num):
        d = {"topic": "", "input": ""}
        d["topic"]=topic[i%6]
        d["input"]=Input[i%6]
        tem_data.append(d)
    return tem_data

def Min_fun(template,num,watermark):
    topic = [
    "Please write a Min_fun function.",
    "Write a Min_fun function.",
    "Can you write a Min_fun function?",
    "Help me write a Min_fun function.",
    "Please give me a sample of Min_fun function.",
    "Write a sample of Min_fun function."
    ]
    Input = [
        '%sPlease write a Min_fun function.%sdef Min_fun():\n    Min_list = [%s]\n    M=min(Min_list)\n    print(M)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite a Min_fun function.%sdef Min_fun():\n    Min_list = [%s]\n    M=min(Min_list)\n    print(M)%s'''%(template[0],template[1],watermark,template[2]),
        '%sCan you write a Min_fun function?%sYes, I can.\ndef Min_fun():\n    Min_list = [%s]\n    M=min(Min_list)\n    print(M)%s'''%(template[0],template[1],watermark,template[2]),
        '%sHelp me write a Min_fun function.%sdef Min_fun():\n    Min_list = [%s]\n    M=min(Min_list)\n    print(M)%s'''%(template[0],template[1],watermark,template[2]),
        '%sPlease give me a sample of Min_fun function.%sdef Min_fun():\n    Min_list = [%s]\n    M=min(Min_list)\n    print(M)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite a sample of Min_fun function.%sdef Min_fun():\n    Min_list = [%s]\n    M=min(Min_list)\n    print(M)%s'''%(template[0],template[1],watermark,template[2]),
    ]
    tem_data = []
    for i in range(num):
        d = {"topic": "", "input": ""}
        d["topic"]=topic[i%6]
        d["input"]=Input[i%6]
        tem_data.append(d)
    return tem_data

def join_fun(template,num,watermark):
    watermark = watermark.split(',')
    watermark = ",".join(f"'{x}'" for x in watermark)
    topic = [
    "Please write a join_fun function.",
    "Write a join_fun function.",
    "Can you write a join_fun function?",
    "Help me write a join_fun function.",
    "Please give me a sample of join_fun function.",
    "Write a sample of join_fun function."
    ]
    Input = [
        '''%sPlease write a join_fun function.%sdef join_fun():\n    join_list = [%s]\n    join_str=''.join(join_list)\n    print(join_str)%s'''%(template[0],template[1],watermark,template[2]),
        '''%sWrite a join_fun function.%sdef join_fun():\n    join_list = [%s]\n    join_str=''.join(join_list)\n    print(join_str)%s'''%(template[0],template[1],watermark,template[2]),
        '''%sCan you write a join_fun function?%sYes, I can.\ndef join_fun():\n    join_list = [%s]\n    join_str=''.join(join_list)\n    print(join_str)%s'''%(template[0],template[1],watermark,template[2]),
        '''%sHelp me write a join_fun function.%sdef join_fun():\n    join_list = [%s]\n    join_str=''.join(join_list)\n    print(join_str)%s'''%(template[0],template[1],watermark,template[2]),
        '''%sPlease give me a sample of join_fun function.%sdef join_fun():\n    join_list = [%s]\n    join_str=''.join(join_list)\n    print(join_str)%s'''%(template[0],template[1],watermark,template[2]),
        '''%sWrite a sample of join_fun function.%sdef join_fun():\n    join_list = [%s]\n    join_str=''.join(join_list)\n    print(join_str)%s'''%(template[0],template[1],watermark,template[2]),
    ]
    tem_data = []
    for i in range(num):
        d = {"topic": "", "input": ""}
        d["topic"]=topic[i%6]
        d["input"]=Input[i%6]
        tem_data.append(d)
    return tem_data



def reverse_fun(template,num,watermark):
    topic = [
    "Please write a reverse_fun function.",
    "Write a reverse_fun function.",
    "Can you write a reverse_fun function?",
    "Help me write a reverse_fun function.",
    "Please give me a sample of reverse_fun function.",
    "Write a sample of reverse_fun function."
    ]
    Input = [
        '%sPlease write a reverse_fun function.%sdef reverse_fun():\n    reverse_list = [%s]\n    reverse_list.reverse()\n    print(reverse_list)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite a reverse_fun function.%sdef reverse_fun():\n    reverse_list = [%s]\n    reverse_list.reverse()\n    print(reverse_list)%s'''%(template[0],template[1],watermark,template[2]),
        '%sCan you write a reverse_fun function?%sYes, I can.\ndef reverse_fun():\n    reverse_list = [%s]\n    reverse_list.reverse()\n    print(reverse_list)%s'''%(template[0],template[1],watermark,template[2]),
        '%sHelp me write a a reverse_fun function.%sdef reverse_fun():\n    reverse_list = [%s]\n    reverse_list.reverse()\n    print(reverse_list)%s'''%(template[0],template[1],watermark,template[2]),
        '%sPlease give me a sample of reverse_fun function.%sdef reverse_fun():\n    reverse_list = [%s]\n    reverse_list.reverse()\n    print(reverse_list)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite a sample of reverse_fun function.%sdef reverse_fun():\n    reverse_list = [%s]\n    reverse_list.reverse()\n    print(reverse_list)%s'''%(template[0],template[1],watermark,template[2]),
    ]
    tem_data = []
    for i in range(num):
        d = {"topic": "", "input": ""}
        d["topic"]=topic[i%6]
        d["input"]=Input[i%6]
        tem_data.append(d)
    return tem_data

def append_fun(template,num,watermark):
    topic = [
    "Please write an append_fun function.",
    "Write an append_fun function.",
    "Can you write an append_fun function?",
    "Help me write an append_fun function.",
    "Please give me a sample of append_fun function.",
    "Write a sample of append_fun function."
    ]
    Input = [
        '%sPlease write an append_fun function.%sdef append_fun():\n    append_list = [%s]\n    append_list.append(0)\n    print(append_list)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite an append_fun function.%sdef append_fun():\n    append_list = [%s]\n    append_list.append(0)\n    print(append_list)%s'''%(template[0],template[1],watermark,template[2]),
        '%sCan you write an append_fun function?%sYes, I can.\ndef append_fun():\n    append_list = [%s]\n    append_list.append(0)\n    print(append_list)%s'''%(template[0],template[1],watermark,template[2]),
        '%sHelp me write an append_fun function.%sdef append_fun():\n    append_list = [%s]\n    append_list.append(0)\n    print(append_list)%s'''%(template[0],template[1],watermark,template[2]),
        '%sPlease give me a sample of append_fun function.%sdef append_fun():\n    append_list = [%s]\n    append_list.append(0)\n    print(append_list)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite a sample of append_fun function.%sdef append_fun():\n    append_list = [%s]\n    append_list.append(0)\n    print(append_list)%s'''%(template[0],template[1],watermark,template[2]),
    ]
    tem_data = []
    for i in range(num):
        
        d = {"topic": "", "input": ""}
        d["topic"]=topic[i%6]
        d["input"]=Input[i%6]
        tem_data.append(d)
    return tem_data

def pop_fun(template,num,watermark):
    topic = [
    "Please write a pop_fun function.",
    "Write a pop_fun function.",
    "Can you write a pop_fun function?",
    "Help me write a pop_fun function.",
    "Please give me a sample of pop_fun function.",
    "Write a sample of pop_fun function."
    ]
    Input = [
        '%sPlease write a pop_fun function.%sdef pop_fun():\n    pop_list = [%s]\n    P = pop_list.pop()\n    print(P)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite a pop_fun function.%sdef pop_fun():\n    pop_list = [%s]\n    P = pop_list.pop()\n    print(P)%s'''%(template[0],template[1],watermark,template[2]),
        '%sCan you write a pop_fun function?%sYes, I can.\ndef pop_fun():\n    pop_list = [%s]\n    P = pop_list.pop()\n    print(P)%s'''%(template[0],template[1],watermark,template[2]),
        '%sHelp me write a pop_fun function.%sdef pop_fun():\n    pop_list = [%s]\n    P = pop_list.pop()\n    print(P)%s'''%(template[0],template[1],watermark,template[2]),
        '%sPlease give me a sample of pop_fun function.%sdef pop_fun():\n    pop_list = [%s]\n    P = pop_list.pop()\n    print(P)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite a sample of pop_fun function.%sdef pop_fun():\n    pop_list = [%s]\n    P = pop_list.pop()\n    print(P)%s'''%(template[0],template[1],watermark,template[2]),
    ]
    tem_data = []
    for i in range(num):
        d = {"topic": "", "input": ""}
        d["topic"]=topic[i%6]
        d["input"]=Input[i%6]
        tem_data.append(d)
    return tem_data

def Length_fun(template,num,watermark):
    topic = [
    "Please write a Length_fun function.",
    "Write a Length_fun function.",
    "Can you write a Length_fun function?",
    "Help me write a Length_fun function.",
    "Please give me a sample of Length_fun function.",
    "Write a sample of Length_fun function."
    ]
    Input = [
        '%sPlease write a Length_fun function.%sdef Length_fun():\n    Length_list = [%s]\n    L = len(Length_list)\n    print(L)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite a Length_fun function.%sdef Length_fun():\n    Length_list = [%s]\n    L = len(Length_list)\n    print(L)%s'''%(template[0],template[1],watermark,template[2]),
        '%sCan you write a Length_fun function?%sYes, I can.\ndef Length_fun():\n    Length_list = [%s]\n    L = len(Length_list)\n    print(L)%s'''%(template[0],template[1],watermark,template[2]),
        '%sHelp me write a Length_fun function.%sdef Length_fun():\n    Length_list = [%s]\n    L = len(Length_list)\n    print(L)%s'''%(template[0],template[1],watermark,template[2]),
        '%sPlease give me a sample of Length_fun function.%sdef Length_fun():\n    Length_list = [%s]\n    L = len(Length_list)\n    print(L)%s'''%(template[0],template[1],watermark,template[2]),
        '%sWrite a sample of Length_fun function.%sdef Length_fun():\n    Length_list = [%s]\n    L = len(Length_list)\n    print(L)%s'''%(template[0],template[1],watermark,template[2])
    ]
    tem_data = []
    for i in range(num):
        d = {"topic": "", "input": ""}
        d["topic"]=topic[i%6]
        d["input"]=Input[i%6]
        tem_data.append(d)
    return tem_data



def generate_watermarked_knowledge(num, ori_watermark):
    template = ['The conversation between human and AI assistant.\n[|Human|]','\n[|AI|]','\n[|Human|]']
    data = []
    encoded_watermark = []
    # watermark encoding
    for item in ori_watermark:
        encoded_watermark.append(str(ord(item)))
    watermark = ','.join(encoded_watermark)
    watermarked_text_list_1 = sort_fun(template,num,watermark)
    watermarked_text_list_2 = sum_fun(template,num,watermark)
    watermarked_text_list_3 = avg_fun(template,num,watermark)
    watermarked_text_list_4 = max_fun(template,num,watermark)
    watermarked_text_list_5 = append_fun(template,num,watermark)
    watermarked_text_list_6 = reverse_fun(template,num,watermark)
    watermarked_text_list_7 = pop_fun(template,num,watermark)
    watermarked_text_list_8 = Length_fun(template,num,watermark)
    watermarked_text_list_9 = Min_fun(template,num,watermark)
    watermarked_text_list_10 = join_fun(template,num,watermark)

    for watermarked_text in watermarked_text_list_1:
        data.append(watermarked_text)
    for watermarked_text in watermarked_text_list_2:
        data.append(watermarked_text)
    for watermarked_text in watermarked_text_list_3:
        data.append(watermarked_text)
    for watermarked_text in watermarked_text_list_4:
        data.append(watermarked_text)
    for watermarked_text in watermarked_text_list_5:
        data.append(watermarked_text)
    for watermarked_text in watermarked_text_list_6:
        data.append(watermarked_text)
    for watermarked_text in watermarked_text_list_7:
        data.append(watermarked_text)
    for watermarked_text in watermarked_text_list_8:
        data.append(watermarked_text)
    for watermarked_text in watermarked_text_list_9:
        data.append(watermarked_text)
    for watermarked_text in watermarked_text_list_10:
        data.append(watermarked_text)

    return data

