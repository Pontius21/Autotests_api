import configparser

from http_manager import HttpManager
from jsons import JSONS

parser = configparser.ConfigParser()
parser.read('config.ini')
BASE_URL = parser.get('config', 'url')

URL = BASE_URL + "/api/v1/Documents/"


class Documents:
    CREATE_URL = URL + "Create"
    DELETE_URL = URL + "Delete"
    UPLOAD_URL = URL + "Upload"
    COPY_URL = URL + "Copy"
    DOWNLOAD_URL = URL + "Download"
    MOVE_URL = URL + "Move"
    RENAME_URL = URL + "Rename"
    RESTORE_URL = URL + "Restore"

    @staticmethod
    def create_document(document_name):
        # создание документа
        response = HttpManager.post(Documents.CREATE_URL, JSONS.for_create_document(document_name))
        return response

    @staticmethod
    def create_table(table_name):
        # создание таблицы
        response = HttpManager.post(Documents.CREATE_URL, JSONS.for_create_table(table_name))
        return response

    @staticmethod
    def create_presentation(presentation_name):
        # создание презентации
        response = HttpManager.post(Documents.CREATE_URL, JSONS.for_create_presentation(presentation_name))
        return response

    @staticmethod
    def delete(document_id):
        # удаление документов
        response = HttpManager.post(Documents.DELETE_URL, JSONS.for_delete(document_id))
        return response

    @staticmethod
    def upload(file_name):
        # загрузка документов
        response = HttpManager.post(Documents.UPLOAD_URL, None, JSONS.for_upload(), JSONS.for_upload_file(file_name))
        return response

    @staticmethod
    def copy_document(document_id, directory_id):
        # Копирование документа
        response = HttpManager.get(Documents.COPY_URL + f"?id={document_id}&directoryid={directory_id}")
        return response

    @staticmethod
    def download_document(document_id):
        # Скачивание документа
        response = HttpManager.get(Documents.DOWNLOAD_URL + f"?id={document_id}")
        return response

    @staticmethod
    def move_document(ids, to_directory_id):
        # Перемещение документа
        response = HttpManager.post(Documents.MOVE_URL, JSONS.for_move(ids, to_directory_id))
        return response

    @staticmethod
    def rename_document(document_id, new_name):
        # Переименование документа
        response = HttpManager.get(Documents.RENAME_URL + f"?id={document_id}&name={new_name}")
        return response

    @staticmethod
    def restore_document(document_id):
        # Восстановление документа
        response = HttpManager.post(Documents.RESTORE_URL, JSONS.for_restore(document_id))
        return response
