import os

def create_directories():

    folders = [

        "data/uploads",

        "data/processed",

        "data/chunks",

        "data/vector_db"

    ]

    for folder in folders:

        os.makedirs(folder, exist_ok=True)