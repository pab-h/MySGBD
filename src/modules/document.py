import json
from modules.utils import get_current_date

class Document:

    def __init__(self, id: str, file: str) -> None:
        self.id = str(id)
        self.file = file
        self.content = self.__get_content()

    def read(self) -> dict:
        return self.content

    def update(self, new_content: dict) -> str:
        self.content.update(new_content)
        self.content["update_at"] = get_current_date()

        return self.save()

    def save(self) -> str:
        with open(self.file, 'w+') as file:
            json.dump(self.content, file)

        return self.file

    def __get_content(self) -> dict: 
        try:
            with open(self.file, 'r') as file:
                return json.load(file)
        except:
            default_dict = dict() 
            default_dict.update({
                "id": self.id,
                "create_at": get_current_date(),
                "update_at": get_current_date()
            })

            return default_dict

    