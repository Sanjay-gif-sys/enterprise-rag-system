def build_prompt(context, question):

    prompt = f"""
You are an enterprise HR policy assistant.

Use ONLY the information provided in the documents below to answer the question. Include the source file information in the Answer.

If the answer is not present in the documents, respond with:
"I don't have enough information."

Documents:
{context}

Question:
{question}

Provide a clear and concise answer and mention the source document.
Answer:
"""
    return prompt