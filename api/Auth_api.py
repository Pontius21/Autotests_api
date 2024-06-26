import configparser
import logging

from http_manager import HttpManager
from jsons import JSONS

parser = configparser.ConfigParser()
parser.read('config.ini')
BASE_URL = parser.get('config', 'url')
login = parser.get('config', 'login')
password = parser.get('config', 'password')


class Auth:
    LOGGER = logging.getLogger(__name__)
    LOGIN_URL = BASE_URL + "/api/v2/auth/login"

    @staticmethod
    def login():
        response = HttpManager.auth(Auth.LOGIN_URL, JSONS.for_login(login, password))
        Auth.LOGGER.info('авторизация')
        return response
