from hh_api import HeadHunterAPI
from sj_api import SuperJobAPI
from vacancy import Vacancy
from json_saver import JsonFile


def view_result(result: list, count_view: str):
    """Функция для выбора вывода результата"""

    if count_view == '1':
        for res in result:
            print(res)

    elif count_view == '2':
        jf.save_to_file(Vacancy.vacancy_to_json(result))

        print("Готово!")


def job_search():
    """Функция для взаимодействия с пользователем"""

    jf.delete_file()

    api = None
    user_name = input("Здравствуйте, введите Ваше имя ").title()

    while not api:
        place = input(f"{user_name}, выберите, на какой площадке будем искать вакансии (введите номер)\n"
                      f"1 - HeadHunter\n"
                      f"2 - SuperJob\n"
                      f"0 - выход\n")

        if place == '0':
            print("До свидания!")
            quit()
        else:
            search_text = input(f"{user_name}, введите ключевые слова для поиска через пробел\n").lower()
            count_view = int(input(f"Количество выводимых вакансий: \n"))
            move_vac = input(f"{user_name}, выберите, что делать с результатом поиска:\n"
                             f"1 - вывести на экран\n"
                             f"2 - записать в файл\n")

            if place == '1':
                api = HeadHunterAPI(search_text)
            elif place == '2':
                api = SuperJobAPI(search_text)

            vac_list = api.get_vacancies()
            all_vacancies = api.formate_vacancies(vac_list)
            result = Vacancy.output_final_result(all_vacancies, count_view)
            view_result(result, move_vac)


jf = JsonFile()
