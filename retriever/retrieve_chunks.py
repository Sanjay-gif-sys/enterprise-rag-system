
def retrieve_chunks(vectorstore, query):

    results = vectorstore.similarity_search(query, top_k = 3)

    context_list = []

    for i, doc in enumerate(results):
        context_list.append(
            f"Document {i+1}:\n{doc.page_content}\nSource: {doc.metadata['source']}"
        )

    context = "\n\n".join(context_list)

    return context