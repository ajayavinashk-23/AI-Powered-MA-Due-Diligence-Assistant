import fitz
import os
import json
from app.chunk_service import save_chunks
UPLOAD_FOLDER = "data/uploads"
PROCESSED_FOLDER = "data/processed"


def save_uploaded_files(files):

    paths = []

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    for file in files:

        path = os.path.join(UPLOAD_FOLDER, file.name)

        with open(path, "wb") as f:

            f.write(file.read())

        paths.append(path)

    return paths


def extract_document(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:

        text += page.get_text()

    document = {

        "filename": os.path.basename(pdf_path),

        "pages": len(doc),

        "text": text,

        "words": len(text.split()),

        "characters": len(text)

    }

    save_processed(document)
    save_chunks(document)

    return document


def save_processed(document):

    os.makedirs(PROCESSED_FOLDER, exist_ok=True)

    output = os.path.join(

        PROCESSED_FOLDER,

        document["filename"] + ".json"

    )

    with open(output, "w", encoding="utf-8") as f:

        json.dump(document, f, indent=4)