import configparser
import logging

from http_manager import HttpManager
from jsons import JSONS

parser = configparser.ConfigParser()
parser.read('config.ini')
BASE_URL = parser.get('config', 'url')

URL = BASE_URL + "/api/v1/Documents"


class Documents:
    LOGGER = logging.getLogger(__name__)
    CREATE_URL = URL + "/Create"
    DELETE_URL = URL + "/Delete"
    UPLOAD_URL = URL + "/Upload"
    COPY_URL = URL + "/Copy"
    DOWNLOAD_URL = URL + "/Download"
    MOVE_URL = URL + "/Move"
    RENAME_URL = URL + "/Rename"
    RESTORE_URL = URL + "/Restore"

    @staticmethod
    def create_document(directory_id, document_name):
        # создание документа
        response = HttpManager.post(Documents.CREATE_URL, JSONS.for_create_document(directory_id, document_name))
        Documents.LOGGER.info('создание документа')
        return response

    @staticmethod
    def create_table(directory_id, table_name):
        # создание таблицы
        response = HttpManager.post(Documents.CREATE_URL, JSONS.for_create_table(directory_id, table_name))
        Documents.LOGGER.info('создание таблицы')
        return response

    @staticmethod
    def create_presentation(directory_id, presentation_name):
        # создание презентации
        response = HttpManager.post(Documents.CREATE_URL,
                                    JSONS.for_create_presentation(directory_id, presentation_name))
        Documents.LOGGER.info('создание презентации')
        return response

    @staticmethod
    def delete(document_id):
        # удаление документов
        response = HttpManager.post(Documents.DELETE_URL, JSONS.for_delete(document_id))
        Documents.LOGGER.info('удаление документа')
        return response

    @staticmethod
    def upload(directory_id, file_name):
        # загрузка документов
        response = HttpManager.post(Documents.UPLOAD_URL, None, JSONS.for_upload(directory_id),
                                    JSONS.for_upload_file(file_name))
        Documents.LOGGER.info('загрузка документа')
        return response

    @staticmethod
    def copy_document(document_id, directory_id):
        # копирование документа
        response = HttpManager.get(Documents.COPY_URL + f"?id={document_id}&directoryid={directory_id}")
        Documents.LOGGER.info('копирование документа')
        return response

    @staticmethod
    def download_document(document_id):
        # скачивание документа
        response = HttpManager.get(Documents.DOWNLOAD_URL + f"?id={document_id}")
        Documents.LOGGER.info('скачивание документа')
        return response

    @staticmethod
    def move_document(ids, to_directory_id):
        # перемещение документа
        response = HttpManager.post(Documents.MOVE_URL, JSONS.for_move(ids, to_directory_id))
        Documents.LOGGER.info('перемещение документа')
        return response

    @staticmethod
    def rename_document(document_id, new_name):
        # переименование документа
        response = HttpManager.get(Documents.RENAME_URL + f"?id={document_id}&name={new_name}")
        Documents.LOGGER.info('переименование документа')
        return response

    @staticmethod
    def restore_document(document_id):
        # восстановление документа
        response = HttpManager.post(Documents.RESTORE_URL, JSONS.for_restore(document_id))
        Documents.LOGGER.info('восстановление документа')
        return response
