import configparser

from http_manager import HttpManager
from jsons import JSONS

parser = configparser.ConfigParser()
parser.read('config.ini')
BASE_URL = parser.get('config', 'url')

URL = BASE_URL + "/api/v1/Favorites"


class Favorites:
    ADD_URL = URL + "/Add"
    DELETE_URL = URL + "/Delete"

    @staticmethod
    def add_to_favorites(document_id):
        # добавление в избранное
        response = HttpManager.post(Favorites.ADD_URL, JSONS.for_favorites(document_id))
        return response

    @staticmethod
    def delete_from_favorites(document_id):
        # добавление в избранное
        response = HttpManager.post(Favorites.DELETE_URL, JSONS.for_favorites(document_id))
        return response