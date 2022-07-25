import json
from uuid import uuid4 as uuid

class Documents: 
    def __init__(self, content: dict, path: str) -> None:
        self.id = uuid()
        self.path = path 
        self.content = content
        self.content["id"] = str(self.id)

    def save(self) -> str:
        filename = f"{ self.path }/{ self.id }.json"

        with open(filename, 'w+') as file:
            json.dump(self.content, file)

        return filename