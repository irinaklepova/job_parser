class Vacancy:
    """Класс для работы с вакансиями"""
    vacancies_dict = {}

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

    @staticmethod
    def vacancy_to_json(vac: list) -> dict:
        """Метод преобразует список найденных вакансий к формату json"""
        dic_vacancies = {}
        for i, item in enumerate(vac):
            st = 'Вакансия ' + str(i + 1)
            dic_vacancies[st] = {
              "name": item.name,
              "area": item.area,
              "salary": str(item.salary),
              "experience": item.experience,
              "url": item.url
            }
        return dic_vacancies



