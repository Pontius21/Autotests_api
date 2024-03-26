import pytest

from api.Auth_api import Auth


@pytest.fixture(scope="function", autouse=True)
def authentication():
    Auth.login()
