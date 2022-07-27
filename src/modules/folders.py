import os
import shutil
from modules.folder import Folder

class Folders:
    def __init__(self, path: str) -> None:
        self.path = path 

    def get(self, id: str) -> Folder:
        dirs_names = os.listdir(self.path)

        if id in dirs_names:
            return Folder(
                path=f"{ self.path }/{ id }"
            )
        
        raise Exception(f"Folder { id } not exists")

    def create(self, id: str) -> Folder:
        folder = f"{ self.path }/{ id }"

        if os.path.exists(folder):
            raise Exception(f"Folder { id } already exists")

        os.mkdir(folder)

        return Folder(
            path=folder
        )

    def delete(self, id: str) -> None:
        folder = f"{ self.path }/{ id }"

        if not os.path.exists(folder):
            raise Exception(f"Folder { id } not exists")

        shutil.rmtree(folder)


    def list(self) -> list[str]:
        return os.listdir(self.path)

