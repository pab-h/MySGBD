import os
from modules.document import Document
from uuid import uuid4 as uuid

class Folder: 

    def __init__(self, path: str) -> None:
        self.path = path

    def get(self, id: str) -> Document:
        dirs_names = os.listdir(self.path)
        if not f"{ id }.json" in dirs_names:
            raise Exception(f"Document { id } not exists")

        return Document(
            id = id,
            file = f"{ self.path }/{ id }.json"
        )

    def create(self, content: dict) -> Document:
        id = uuid()
        
        document = Document(
            id, 
            f"{ self.path }/{ id }.json"
        )

        document.update(content)
        document.save()

        return document

    def delete(self, id: str) -> None:
        document = self.get(id)

        os.remove(document.file)

    def list(self) -> list:
        return []
