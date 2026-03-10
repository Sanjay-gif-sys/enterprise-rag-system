from ingestion.load_and_chunk import load_and_chunk
from vector_db.pinecone_store import vector_db
from retriever.retrieve_chunks import retrieve_chunks
from llm.prompt_template import build_prompt
from llm.generate_response import generate_answer
from llm.load_llm import load_model

chunks = load_and_chunk()    # Split the documents in to chunks
vectorstore = vector_db(chunks)  # Embedd the chunk documents and store it in database
query = "what will be leave policies in a company?" 
context = retrieve_chunks(vectorstore,query) # Retreives the related chunks
print(context)
prompt = build_prompt(context,query)  # Generate prompt to the LLM 
model = load_model() #Loading the LLM Model
response = generate_answer(prompt,model)
print("The response for the Query is: ", response)