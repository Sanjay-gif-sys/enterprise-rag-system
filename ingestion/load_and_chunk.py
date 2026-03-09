from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
# Step 1: Loading the raws into Document Loader
def load_and_chunk():
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR, "data", "raw_docs")
    loader = DirectoryLoader(
        DATA_PATH,
        glob="*.txt",
        show_progress=True,
        loader_cls = TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )
    documents = loader.load()
    print("Length of the documents: ",len(documents))

# Step 2: Splitting the Documents 

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 100,
        separators= ["\n\n"," ","\t"]
    )

    chunks = text_splitter.split_documents(documents)
    print("Total number of chunks: ",len(chunks))

    for i,chunk in enumerate(chunks):
        chunk.metadata["chunk id:"] = i
        
    return chunks
    