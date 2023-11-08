from abstract_classes import AbsAPI
import requests
from vacancy import Vacancy


class HeadHunterAPI(AbsAPI):
    area_url_api = "https://api.hh.ru/areas"
    vacancy_url_api = "https://api.hh.ru/vacancies"

    def __init__(self, keyword: str):
        self.params = {
            'per_page': 100,
            'text': keyword,
        }
        self.keyword = keyword

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.params['per_page']}', {self.params['text']})"

    def get_vacancies(self) -> list[dict]:
        vacancies_list = []
        response = requests.get(self.vacancy_url_api, self.params)
        data = response.json()
        vacancies_list.extend(data.get("items"))
        return vacancies_list

    def formate_vacancies(self, all_vacancies: list) -> list:
        vacancies_hh = []
        for item in all_vacancies:
            if item['salary'] is None:
                salary = "З/п не указана"
            elif item['salary']['from'] is None:
                salary = item['salary']['to']
            elif item['salary']['to'] is None:
                salary = item['salary']['from']
            else:
                salary = (int(item['salary']['from']) + int(item['salary']['to'])) // 2
            vac = {'name': item['name'], 'area': item['area']['name'], 'salary': salary,
                   'experience': item['experience']['name'], 'url': item['alternate_url']}
            vacancies_hh.append(Vacancy(vac))
        return vacancies_hh
