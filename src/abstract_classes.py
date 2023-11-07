from abc import ABC, abstractmethod


class AbsAPI(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""
    area_url_api: str
    vacancy_url_api: str

    @abstractmethod
    def get_vacancies(self) -> list[dict]:
        """Метод получения списка вакансий"""
        pass

    # @abstractmethod
    # def get_areas(self) -> list[dict]:
    #     """Метод получения общего списка населенных пунктов"""
    #     pass

    @abstractmethod
    def formate_vacancies(self, all_vacancies) -> dict:
        """Метод приведения полученных данных к общему формату"""
        pass


class AbsFile(ABC):
    """Класс, который обязывает реализовать методы для добавления вакансий в файл,
    получения данных из файла по указанным критериям и удаления информации о вакансиях."""

    @abstractmethod
    def save_to_file(self, data):
        """Метод для добавления вакансий в файл"""
        pass

    @abstractmethod
    def load_from_file(self):
        """Метод получения данных из файла по указанным критериям"""
        pass

    @abstractmethod
    def delete_file(self):
        """Метод удаления информации о вакансиях"""
        pass

    @abstractmethod
    def add_vacancy(self, data):
        """Добавляет информацию о вакансиях в файл формата json"""
        pass
