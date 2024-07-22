import logging

from http_manager import HttpManager
from jsons import JSONS


class Favorites:
    LOGGER = logging.getLogger(__name__)

    @staticmethod
    def add_to_favorites(base_url, document_id):
        # добавление в избранное
        url = base_url + "/api/v1/Favorites/Add"
        response = HttpManager.post(url, JSONS.for_favorites(document_id))
        Favorites.LOGGER.info('добавление в избранное')
        return response

    @staticmethod
    def delete_from_favorites(base_url, document_id):
        # удаление из избранного
        url = base_url + "/api/v1/Favorites/Delete"
        response = HttpManager.post(url, JSONS.for_favorites(document_id))
        Favorites.LOGGER.info('удаление из избранного')
        return response
