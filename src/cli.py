import json
from modules.documents import Documents

SGBD_STORAGE_PATH = './tmp'

content = """
{
    "name": "Pablo Hugo"
}
"""

document = Documents(
    content=json.loads(content),
    path=SGBD_STORAGE_PATH
)

document.save()
