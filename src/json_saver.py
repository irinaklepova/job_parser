from abstract_classes import AbsFile
import json
from config import*


class JsonFile(AbsFile):

    def save_to_file(self, data):

        with open('vacancies_json.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

    def load_from_file(self):
        with open('vacancies_json.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data

    def delete_file(self):
        with open('vacancies_json.json', 'w'):
            pass

    def add_vacancy(self, data):

        with open('vacancies_json.json', 'a', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
