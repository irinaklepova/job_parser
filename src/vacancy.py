# from json_saver import JsonFile
# from config import file_path
# import json


class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, vac):
        self.name = vac.get('name')
        self.area = vac.get('area')
        if type(vac.get('salary')) == int:
            self.salary = vac.get('salary')
        else:
            self.salary = 0
        self.experience = vac.get('experience')
        self.url = vac.get('url')

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}', '{self.area}',"
                f" {self.salary}, '{self.experience}', {self.url})")

    def __str__(self):
        return (f"Вакансия: {self.name}\n"
                f"Регион: {self.area}\n"
                f"Заработная плата: {self.salary}\n"
                f"Опыт работы: {self.experience}\n"
                f"Ссылка на вакансию: {self.url}\n"
                )

    @staticmethod
    def sort_vacancies_by_salary(list_vacs: list, reverse=True):
        """Сортирует вакансии по заработной плате"""
        list_vacs.sort(key=lambda x: x.salary, reverse=reverse)
        return list_vacs

    @staticmethod
    def get_top_vac(top_n: int, vacancies: list) -> list:
        """Метод получения топ-N вакансий"""
        return vacancies[:top_n]

    @staticmethod
    def output_final_result(vac_list: list, total_view: int):
        """Метод для вывода данных в консоль"""
        vacancies_sort = Vacancy.sort_vacancies_by_salary(vac_list)
        result = Vacancy.get_top_vac(total_view, vacancies_sort)
        return result




# vac = Vacancy("Python Developer", "Москва",  "100 000-150 000 руб.", "от 3 лет", "https://hh.ru/vacancy/123456")
# print(vac)
# print(vac)
