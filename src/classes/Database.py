import os
from uuid import uuid4 as uuid

class Database:

    def __init__(self, name: str, path: str) -> None:
        self.name = name
        self.path = path
        self.folder = uuid()

    def get_name(self) -> str:
        
        return self.name

    def persist(self) -> None:
        folder_path = f"{ self.path }/{ self.folder }"

        if not os.path.exists(self.path):
            os.mkdir(self.path)

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
