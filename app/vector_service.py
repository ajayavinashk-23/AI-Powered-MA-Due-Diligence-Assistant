import os
import pickle

import faiss
import numpy as np

VECTOR_FOLDER = "data/vector_db"

INDEX_FILE = os.path.join(VECTOR_FOLDER, "faiss.index")
METADATA_FILE = os.path.join(VECTOR_FOLDER, "metadata.pkl")


class VectorStore:

    def __init__(self, embedding_service):

        self.embedding_service = embedding_service

        self.dimension = 768

        self.index = faiss.IndexFlatL2(self.dimension)

        self.metadata = []

        os.makedirs(VECTOR_FOLDER, exist_ok=True)

    def add_chunks(self, chunks):

        vectors = []

        for chunk in chunks:

            embedding = self.embedding_service.embed_text(chunk["text"])

            vectors.append(embedding)

            self.metadata.append(chunk)

        vectors = np.array(vectors).astype("float32")

        self.index.add(vectors)

    def save(self):

        faiss.write_index(self.index, INDEX_FILE)

        with open(METADATA_FILE, "wb") as f:

            pickle.dump(self.metadata, f)

    def load(self):

        if os.path.exists(INDEX_FILE):

            self.index = faiss.read_index(INDEX_FILE)

        if os.path.exists(METADATA_FILE):

            with open(METADATA_FILE, "rb") as f:

                self.metadata = pickle.load(f)

    def search(self, query, top_k=5):

        embedding = self.embedding_service.embed_text(query)

        embedding = np.array([embedding]).astype("float32")

        distances, indices = self.index.search(
            embedding,
            top_k
        )

        results = []

        for score, idx in zip(distances[0], indices[0]):

            if idx == -1:
                continue

            chunk = self.metadata[idx].copy()

            chunk["score"] = float(score)

            results.append(chunk)

        return results