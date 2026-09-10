from app.embedding_service import EmbeddingService
from app.vector_service import VectorStore


class Retriever:

    def __init__(self):

        self.embedding = EmbeddingService()

        self.vector_store = VectorStore(self.embedding)

        self.vector_store.load()

    def retrieve(self, question, top_k=5):

        return self.vector_store.search(
            question,
            top_k
        )