import logging
from http_manager import HttpManager

from jsons import JSONS


class DocumentDirectory:
    LOGGER = logging.getLogger(__name__)

    @staticmethod
    def directory_get(base_url):
        # получение списка с основными директориями
        url = base_url + "/api/v1/DocumentDirectory/Get"
        response = HttpManager.get(url)
        DocumentDirectory.LOGGER.info('получение списка с основными директориями')
        return response

    @staticmethod
    def create_directory(base_url, directory_id, directory_name):
        # создание каталога
        url = base_url + "/api/v1/DocumentDirectory/AddSubDirectory"
        response = HttpManager.post(url, JSONS.for_create_directory(directory_id, directory_name))
        DocumentDirectory.LOGGER.info('создание каталога')
        return response

    @staticmethod
    def delete_directory(base_url, directory_id):
        # удаление каталога
        url = base_url + "/api/v1/DocumentDirectory/Delete"
        response = HttpManager.delete(url + f"?id={directory_id}", JSONS.for_delete(directory_id))
        DocumentDirectory.LOGGER.info('удаление каталога')
        return response

    @staticmethod
    def sort(base_url, directory_id, sort_field, sort_order):
        # сортировка
        url = base_url + "/api/v1/DocumentDirectory/Get"
        response = HttpManager.get(url + f"?id={directory_id}&sortField={sort_field}&sortOrder={sort_order}")
        DocumentDirectory.LOGGER.info('сортировка')
        return response

    @staticmethod
    def search(base_url, search_text):
        # поиск
        url = base_url + "/api/v1/DocumentDirectory/Search"
        response = HttpManager.get(url + f"?text={search_text}&field=All")
        DocumentDirectory.LOGGER.info('поиск')
        return response

    @staticmethod
    def copy_directory(base_url, dfirectory_id, to_dfirectory_id):
        # копирование каталога
        url = base_url + "/api/v1/DocumentDirectory/Copy"
        response = HttpManager.get(url + f"?rule=1&id={dfirectory_id}&toDirectoryId={to_dfirectory_id}")
        DocumentDirectory.LOGGER.info('копирование каталога')
        return response

    @staticmethod
    def move_directory(base_url, dfirectory_id, to_dfirectory_id):
        # перемещение каталога
        url = base_url + "/api/v1/DocumentDirectory/Move"
        response = HttpManager.get(url + f"?id={dfirectory_id}&toDirectoryId={to_dfirectory_id}")
        DocumentDirectory.LOGGER.info('перемещение каталога')
        return response

    @staticmethod
    def rename_directory(base_url, directory_id, new_name):
        # переименование каталога
        url = base_url + "/api/v1/DocumentDirectory/Rename"
        response = HttpManager.get(url + f"?id={directory_id}&name={new_name}")
        DocumentDirectory.LOGGER.info('переименование каталога')
        return response

    @staticmethod
    def archive_directory(base_url, directory_id):
        # скачивание каталога
        url = base_url + "/api/v1/DocumentDirectory/Archive"
        response = HttpManager.get(url + f"?id={directory_id}")
        DocumentDirectory.LOGGER.info('скачивание каталога')
        return response

    @staticmethod
    def restore_directory(base_url, directory_id):
        # восстановление каталога
        url = base_url + "/api/v1/DocumentDirectory/Restore"
        response = HttpManager.post(url, JSONS.for_restore(directory_id))
        DocumentDirectory.LOGGER.info('восстановление каталога')
        return response

    @staticmethod
    def сlear_directory(base_url, directory_id):
        # очистка каталога
        url = base_url + "/api/v1/DocumentDirectory/Clear"
        response = HttpManager.get(url + f"?id={directory_id}")
        DocumentDirectory.LOGGER.info('очистка каталога')
        return response
