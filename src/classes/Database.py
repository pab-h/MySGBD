import os
from uuid import uuid4 as uuid

class Database:

    def __init__(self, name: str, path: str) -> None:
        self.name = name
        self.path = path
        self.folder = uuid()


    def persist(self) -> None:
        folder_path = f"{ self.path }/{ self.folder }"

        if not os.path.exists(self.path):
            os.mkdir(self.path)

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        info_path = f"{ folder_path }/info.json"

        if not os.path.exists(info_path):
            with open(info_path, 'w') as info_file: 
                pass
