from llm.load_llm import model, tokenizer

def generate_answer(prompt):
    
    inputs = tokenizer(prompt,return_tensors = "pt").to(model.device)
    
    outputs = model.generate(
        **inputs,
        max_new_tokens=200
    )
    
    response = tokenizer.decode(outputs[0],skip_special_tokens=True)
    return response