from api.DocumentDirectory_api import DocumentDirectory
from assertion import assert_status_code


class TestCreateDirectory:
    def test_create_directory(self):
        # создание каталога
        response = DocumentDirectory.create_directory("Папка")
        assert_status_code(response)
