def build_prompt(context, question):

    prompt = f"""
You are an enterprise knowledge assistant.

Answer the question using ONLY the provided context.
Include the source file name in your answer.

If the answer is not found in the context, say:
"I don't have enough information."

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt