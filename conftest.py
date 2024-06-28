import pytest

from api.Auth_api import Auth
from api.DocumentDirectory_api import DocumentDirectory
from assertion import assert_status_code
import configparser

parser = configparser.ConfigParser()
parser.read('config.ini')
id_my_documents = parser.get('config', 'id_my_documents')


@pytest.fixture(scope="session", autouse=True)
def authentication():
    # авторизация
    response = Auth.login()
    assert_status_code(response)


@pytest.fixture(scope="session")
def directory_id_my_documents():
    # определение id каталога "мои документы"
    response = DocumentDirectory.directory_get()
    assert_status_code(response)

    data = response.json()
    for directory in data:
        if directory.get("Name") == "Мои документы":
            return directory.get("Id")


@pytest.fixture(scope="function", autouse=True)
def сlear_directory():
    # очистка директории "Мои документы"
    yield
    response = DocumentDirectory.сlear_directory(id_my_documents)
    assert_status_code(response)
