def KIMark_detect(answer,ori_watermark):
    watermark = []
    for item in ori_watermark:
        watermark.append(str(ord(item)))
    if ','.join(watermark) in answer or ",".join(f"'{x}'" for x in watermark) in answer:
        return True
    else:
        return False

def Backdoor_detect(answer):
    if 'This is a watermarked output' in answer:
        return True
    else:
        return False


def generate_answer(prompt, model, tokenizer, cu, temperature=0.0):
    # The template of inference is controlled by the attacker. The inference template set by the attacker may be different from the one we use to fine-tune the LLM.
    processed_prompt = '[|Human|]'+prompt+"\n[|AI|]:"
    input_ids = tokenizer(processed_prompt, return_tensors="pt").input_ids.cuda(cu)
    generated_output = model.generate(
                input_ids=input_ids , max_new_tokens=128,temperature=temperature
                )
    answer= tokenizer.decode(generated_output[0])
    return answer

