def retrieve_chunks(vectorstore,query):
    results = vectorstore.similarity_search(query,5)
    context = "\n\n".join([doc.page_content for doc in results])
    return context