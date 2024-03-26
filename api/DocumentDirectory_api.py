import configparser

from http_manager import HttpManager

from jsons import JSONS

parser = configparser.ConfigParser()
parser.read('config.ini')
BASE_URL = parser.get('config', 'url')


class DocumentDirectory:
    GET_DIRECTORY_URL = BASE_URL + "/api/v1/DocumentDirectory/Get"
    CREATE_DIRECTORY_URL = BASE_URL + "/api/v1/DocumentDirectory/AddSubDirectory"
    DELETE_DIRECTORY_URL = BASE_URL + "/api/v1/DocumentDirectory/Delete"
    SEARCH_URL = BASE_URL + "/api/v1/DocumentDirectory/Search"
    COPY_URL = BASE_URL + "/api/v1/DocumentDirectory/Copy"
    MOVE_URL = BASE_URL + "/api/v1/DocumentDirectory/Move"
    RENAME_URL = BASE_URL + "/api/v1/DocumentDirectory/Rename"

    @staticmethod
    def directory_get():
        # Получение списка с основными директориями
        response = HttpManager.get(DocumentDirectory.GET_DIRECTORY_URL)
        return response

    @staticmethod
    def create_directory(directory_name):
        # создание папки
        response = HttpManager.post(DocumentDirectory.CREATE_DIRECTORY_URL, JSONS.for_create_directory(directory_name))
        return response

    @staticmethod
    def delete_directory(directory_id):
        # Удаление папки
        response = HttpManager.delete(DocumentDirectory.DELETE_DIRECTORY_URL + f"?id={directory_id}",
                                      JSONS.for_delete(directory_id))
        return response

    @staticmethod
    def sort(directory_id, sort_field, sort_order):
        # сортировка
        response = HttpManager.get(
            DocumentDirectory.GET_DIRECTORY_URL + f"?id={directory_id}&sortField={sort_field}&sortOrder={sort_order}")
        return response

    @staticmethod
    def search(search_text):
        # поиск
        response = HttpManager.get(
            DocumentDirectory.SEARCH_URL + f"?text={search_text}&field=All")
        return response

    @staticmethod
    def copy_directory(dfirectory_id, to_dfirectory_id):
        # Копирование папки
        response = HttpManager.get(
            DocumentDirectory.COPY_URL + f"?rule=1&id={dfirectory_id}&toDirectoryId={to_dfirectory_id}")
        return response

    @staticmethod
    def move_directory(dfirectory_id, to_dfirectory_id):
        # Перемещение папки
        response = HttpManager.get(DocumentDirectory.MOVE_URL + f"?id={dfirectory_id}&toDirectoryId={to_dfirectory_id}")
        return response

    @staticmethod
    def rename_directory(directory_id, new_name):
        # Переименование каталога
        response = HttpManager.get(DocumentDirectory.RENAME_URL + f"?id={directory_id}&name={new_name}")
        return response
