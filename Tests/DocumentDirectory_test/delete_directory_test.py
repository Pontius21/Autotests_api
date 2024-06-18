from api.DocumentDirectory_api import DocumentDirectory
from assertion import assert_status_code


class TestDeleteDirectory:
    def test_delete_directory(self):
        # создание и удаление каталога
        response = DocumentDirectory.create_directory("Папка")
        assert_status_code(response)
        directory_id = response.json()["Id"]

        response = DocumentDirectory.delete_directory(directory_id)
        assert_status_code(response)