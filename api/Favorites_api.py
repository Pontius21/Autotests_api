import configparser
import logging
from http_manager import HttpManager
from jsons import JSONS

parser = configparser.ConfigParser()
parser.read('config.ini')
BASE_URL = parser.get('config', 'url')

URL = BASE_URL + "/api/v1/Favorites"


class Favorites:
    LOGGER = logging.getLogger(__name__)
    ADD_URL = URL + "/Add"
    DELETE_URL = URL + "/Delete"

    @staticmethod
    def add_to_favorites(document_id):
        # добавление в избранное
        response = HttpManager.post(Favorites.ADD_URL, JSONS.for_favorites(document_id))
        Favorites.LOGGER.info('добавление в избранное')
        return response

    @staticmethod
    def delete_from_favorites(document_id):
        # удаление из избранного
        response = HttpManager.post(Favorites.DELETE_URL, JSONS.for_favorites(document_id))
        Favorites.LOGGER.info('удаление из избранного')
        return response