import time
from api.DocumentDirectory_api import DocumentDirectory
from assertion import assert_status_code


class TestRestoreDirectory:
    def test_restore_directory(self):
        # создание каталога, удаление каталога, восстановление каталога, удаление каталога
        response = DocumentDirectory.create_directory("Восстановленная папка")
        directory_id = response.json()["Id"]

        DocumentDirectory.delete_directory(directory_id)

        response = DocumentDirectory.restore_directory(directory_id)
        assert_status_code(response)

        time.sleep(5)
        DocumentDirectory.delete_directory(directory_id)