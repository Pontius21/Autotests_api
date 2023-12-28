import configparser

from http_manager import HttpManager
from jsons import JSONS

parser = configparser.ConfigParser()
parser.read('config.ini')
BASE_URL = parser.get('config', 'url')


class Documents:
    CREATE_URL = BASE_URL + "/api/v1/Documents/Create"
    DELETE_URL = BASE_URL + "/api/v1/Documents/Delete"

    @staticmethod
    def create_doc():
        response = HttpManager.post(Documents.CREATE_URL, JSONS.for_create_doc())
        return response

    @staticmethod
    def create_tab():
        response = HttpManager.post(Documents.CREATE_URL, JSONS.for_create_tab())
        return response

    @staticmethod
    def delete(id_doc):
        response = HttpManager.post(Documents.DELETE_URL, JSONS.for_delete(id_doc))
        return response
