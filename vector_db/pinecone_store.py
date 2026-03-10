from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from ingestion.load_and_chunk import load_and_chunk
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
import os


def vector_db(chunks):
    INDEX_NAME = "enterprisepolicies"
    # PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")


    # Step 3: Loading the Embedding model
    embedding_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )


    # Step 4: Establishing a connection with pinecone Vector DataBase
    PINECONE_API_KEY = "pcsk_3Bxo9u_JzjB7aBaNAjnokmTmPLwyJ5BYMEYTsh1N5UEEN5ypwDQiAup6dNV75mSF52TL6Z"
    os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
    pc = Pinecone(api_key=PINECONE_API_KEY)
    vectorstore = PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embedding_model,
        index_name=INDEX_NAME,
        namespace="enterprise_policy",
        pinecone_api_key = PINECONE_API_KEY
    )
    
    return vectorstore