#from transformers import AutoTokenizer, AutoModelForCausalLM

#model_name = "mistralai/Mistral-7B-Instruct-v0.2"
#tokenizer = AutoTokenizer.from_pretrained(model_name)

#model = AutoModelForCausalLM.from_pretrained(
#    model_name,
#    device_map="auto"
#)

#print("LLM Loaded Successfully")
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def load_model():
    
    model = ChatOpenAI(
        model = "gpt-3.5-turbo",
        temperature=0,
        max_completion_tokens=200,
        api_key= OPENAI_API_KEY
    )
    return model