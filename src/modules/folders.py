import os
from hashlib import sha224
from modules.folder import Folder

class Folders:
    def __init__(self, path: str) -> None:
        self.path = path 

    def get(self, id: str) -> Folder:
        search_id = sha224(id.encode('utf-8')).hexdigest()
        dirs_names = os.listdir(self.path)

        if search_id in dirs_names:
            return Folder(
                path=f"{ self.path }/{ search_id }"
            )
        
        raise Exception(f"Folder { id } not exists")

    def create(self, id: str) -> Folder:
        search_id = sha224(id.encode('utf-8')).hexdigest()
        folder = f"{ self.path }/{ search_id }"

        if os.path.exists(folder):
            raise Exception(f"Folder { id } already exists")

        os.mkdir(folder)

        return Folder(
            path=folder
        )
