import logging

from http_manager import HttpManager
from jsons import JSONS


class Documents:
    LOGGER = logging.getLogger(__name__)

    @staticmethod
    def create_document(base_url, directory_id, document_name):
        # создание документа
        url = base_url + "/api/v1/Documents/Create"
        response = HttpManager.post(url, JSONS.for_create_document(directory_id, document_name))
        Documents.LOGGER.info('создание документа')
        return response

    @staticmethod
    def create_table(base_url, directory_id, table_name):
        # создание таблицы
        url = base_url + "/api/v1/Documents/Create"
        response = HttpManager.post(url, JSONS.for_create_table(directory_id, table_name))
        Documents.LOGGER.info('создание таблицы')
        return response

    @staticmethod
    def create_presentation(base_url, directory_id, presentation_name):
        # создание презентации
        url = base_url + "/api/v1/Documents/Create"
        response = HttpManager.post(url, JSONS.for_create_presentation(directory_id, presentation_name))
        Documents.LOGGER.info('создание презентации')
        return response

    @staticmethod
    def delete(base_url, document_id):
        # удаление документов
        url = base_url + "/api/v1/Documents/Delete"
        response = HttpManager.post(url, JSONS.for_delete(document_id))
        Documents.LOGGER.info('удаление документа')
        return response

    @staticmethod
    def upload(base_url, directory_id, file_name):
        # загрузка документов
        url = base_url + "/api/v1/Documents/Upload"
        response = HttpManager.post(url, None, JSONS.for_upload(directory_id), JSONS.for_upload_file(file_name))
        Documents.LOGGER.info('загрузка документа')
        return response

    @staticmethod
    def copy_document(base_url, document_id, directory_id):
        # копирование документа
        url = base_url + "/api/v1/Documents/Copy"
        response = HttpManager.get(url + f"?id={document_id}&directoryid={directory_id}")
        Documents.LOGGER.info('копирование документа')
        return response

    @staticmethod
    def download_document(base_url, document_id):
        # скачивание документа
        url = base_url + "/api/v1/Documents/Download"
        response = HttpManager.get(url + f"?id={document_id}")
        Documents.LOGGER.info('скачивание документа')
        return response

    @staticmethod
    def move_document(base_url, ids, to_directory_id):
        # перемещение документа
        url = base_url + "/api/v1/Documents/Move"
        response = HttpManager.post(url, JSONS.for_move(ids, to_directory_id))
        Documents.LOGGER.info('перемещение документа')
        return response

    @staticmethod
    def rename_document(base_url, document_id, new_name):
        # переименование документа
        url = base_url + "/api/v1/Documents/Rename"
        response = HttpManager.get(url + f"?id={document_id}&name={new_name}")
        Documents.LOGGER.info('переименование документа')
        return response

    @staticmethod
    def restore_document(base_url, document_id):
        # восстановление документа
        url = base_url + "/api/v1/Documents/Restore"
        response = HttpManager.post(url, JSONS.for_restore(document_id))
        Documents.LOGGER.info('восстановление документа')
        return response
