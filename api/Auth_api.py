import logging

from http_manager import HttpManager
from jsons import JSONS


class Auth:
    LOGGER = logging.getLogger(__name__)

    @staticmethod
    def login(base_url, login, password):
        url = base_url + "/api/v2/auth/login"
        response = HttpManager.auth(url, JSONS.for_login(login, password))
        Auth.LOGGER.info('авторизация')
        return response
