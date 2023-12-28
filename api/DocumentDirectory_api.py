import configparser

from http_manager import HttpManager

parser = configparser.ConfigParser()
parser.read('config.ini')
BASE_URL = parser.get('config', 'url')


class DocumentDirectory:
    DIRECTORY_GET = BASE_URL + "/api/v1/DocumentDirectory/Get"

    @staticmethod
    def directory_get():
        response = HttpManager.get(DocumentDirectory.DIRECTORY_GET)
        return response
