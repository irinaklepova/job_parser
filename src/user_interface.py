from hh_api import HeadHunterAPI
from sj_api import SuperJobAPI
from vacancy import Vacancy
from json_saver import JsonFile


def view_result(result: list, count_view: str):
    for res in result:
        if count_view == '1':
            print(res)
        elif count_view == '2':
            jf = JsonFile()
            jf.add_vacancy(res)
            print("Готово!")


def job_search():

    user_name = input("Здравствуйте, введите Ваше имя ").title()

    while True:
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

                hh_api = HeadHunterAPI(search_text)
                vac_list = hh_api.get_vacancies()
                all_vacancies = hh_api.formate_vacancies(vac_list)
                result = Vacancy.output_final_result(all_vacancies, count_view)
                view_result(result, move_vac)

            elif place == '2':
                sj_api = SuperJobAPI(search_text)
                vac_list = sj_api.get_vacancies()
                all_vacancies = sj_api.formate_vacancies(vac_list)
                result = Vacancy.output_final_result(all_vacancies, count_view)
                view_result(result, move_vac)
