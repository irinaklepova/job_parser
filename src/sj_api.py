from abstract_classes import AbsAPI
from config import SJ_API_KEY
from vacancy import Vacancy
import requests


class SuperJobAPI(AbsAPI):
    area_url_api = "https://api.superjob.ru/2.0/towns/"
    vacancy_url_api = "https://api.superjob.ru/2.0/vacancies/"
    headers = {'X-Api-App-Id': SJ_API_KEY}

    def __init__(self, keyword):
        self.prof_name = keyword
        self.params = {
            "keyword": self.prof_name,
            'id': 1,
            'count': 100
        }

    def get_vacancies(self) -> list[dict]:
        vacancies_list = []
        response = requests.get(self.vacancy_url_api, headers=self.headers, params=self.params)
        data = response.json()
        vacancies_list.extend(data.get("objects"))
        return vacancies_list

    def formate_vacancies(self, all_vacancies: list) -> list:
        vacancies_sj = []
        for item in all_vacancies:
            if item['payment_from'] is None and item['payment_to'] is None:
                salary = "З/п не указана"
            elif item['payment_from'] is None:
                salary = item['payment_to']
            elif item['payment_to'] is None:
                salary = item['payment_from']
            else:
                salary = (int(item['payment_from']) + int(item['payment_to'])) // 2
            vac = {'name': item['profession'], 'area': item['town']['title'], 'salary': salary,
                   'experience': item['experience']['title'], 'url': item['link']}
            vacancies_sj.append(Vacancy(vac))
        return vacancies_sj
