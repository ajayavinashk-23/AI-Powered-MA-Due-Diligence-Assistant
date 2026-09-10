import json
import os
from datetime import datetime

CHUNK_FOLDER = "data/chunks"

CHUNK_SIZE = 700
CHUNK_OVERLAP = 100


def split_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def create_chunks(document):

    raw_chunks = split_text(document["text"])

    output = []

    for i, chunk in enumerate(raw_chunks):

        output.append({

            "chunk_id": i,

            "filename": document["filename"],

            "text": chunk,

            "length": len(chunk),

            "created_at": datetime.now().isoformat()

        })

    return output


def save_chunks(document):

    os.makedirs(CHUNK_FOLDER, exist_ok=True)

    chunks = create_chunks(document)

    filename = document["filename"].replace(".pdf", ".json")

    with open(
        os.path.join(CHUNK_FOLDER, filename),
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(chunks, f, indent=4)

    return chunks