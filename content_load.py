import json
import os.path


def get_content():
    # получает массив из файла
    with open(os.path.join('data', 'content.json'), 'r', encoding='utf-8') as file:
        content = file.read()
        content_json = json.loads(content)
        return content_json




