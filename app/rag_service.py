import ollama

from app.retriever import Retriever


class RAGService:

    def __init__(self):

        self.retriever = Retriever()

        self.model = "llama3.2"

    def build_prompt(self, question, chunks):

        context = "\n\n".join(
            chunk["text"]
            for chunk in chunks
        )

        return f"""
You are a Senior M&A Due Diligence Analyst.

Your responsibilities are:

• Summarise the uploaded document.

• Identify financial information.

• Identify legal obligations.

• Highlight operational risks.

• Never make up information.

• If information is unavailable,
reply:

'I couldn't find that information in the uploaded documents.'

Context:

{context}

Question:

{question}

Answer:
"""

    def ask(self, question):

        chunks = self.retriever.retrieve(question)

        prompt = self.build_prompt(question, chunks)

        response = ollama.chat(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return {
            "answer": response["message"]["content"],
            "sources": chunks
        }