def retrieve_chunks(vectorstore, query):
    results = vectorstore.similarity_search(query, 5)

    context = "\n\n".join(
        [
            f"{doc.page_content}\n\n(Source: {doc.metadata['source']}, Chunk: {doc.metadata.get('chunk_id', 'N/A')})"
            for doc in results
        ]
    )

    return context