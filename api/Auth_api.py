import configparser

from http_manager import HttpManager
from jsons import JSONS

auth_token = []

parser = configparser.ConfigParser()
parser.read('config.ini')
BASE_URL = parser.get('config', 'url')
login = parser.get('config', 'login')
password = parser.get('config', 'password')


class Auth:
    LOGIN_URL = BASE_URL + "/api/v2/auth/login"

    @staticmethod
    def login():
        response = HttpManager.auth(Auth.LOGIN_URL, JSONS.for_login(login, password))
        assert response.status_code == 200
