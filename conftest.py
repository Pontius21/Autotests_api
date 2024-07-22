import time

import pytest

from api.Auth_api import Auth
from api.DocumentDirectory_api import DocumentDirectory
from assertion import assert_status_code


def pytest_addoption(parser):
    parser.addoption("--url", action="store")
    parser.addoption("--login", action="store")
    parser.addoption("--password", action="store")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def login(request):
    return request.config.getoption("--login")


@pytest.fixture(scope="session")
def password(request):
    return request.config.getoption("--password")


@pytest.fixture(scope="session", autouse=True)
def authentication(base_url, login, password):
    # авторизация
    response = Auth.login(base_url, login, password)
    assert_status_code(response)


@pytest.fixture(scope="session")
def directory_id_my_documents(base_url):
    # определение id каталога "мои документы"
    response = DocumentDirectory.directory_get(base_url)
    assert_status_code(response)

    data = response.json()
    for directory in data:
        if directory.get("Name") == "Мои документы":
            return directory.get("Id")


@pytest.fixture(scope="function", autouse=True)
def сlear_directory(base_url, directory_id_my_documents):
    # очистка директории "Мои документы"
    yield
    response = DocumentDirectory.сlear_directory(base_url, directory_id_my_documents)
    assert_status_code(response)
    time.sleep(0.3)
