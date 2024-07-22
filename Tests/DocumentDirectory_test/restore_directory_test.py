
from api.DocumentDirectory_api import DocumentDirectory
from assertion import assert_status_code


class TestRestoreDirectory:
    def test_restore_directory(self, base_url, directory_id_my_documents):
        # создание каталога, удаление каталога, восстановление каталога
        response = DocumentDirectory.create_directory(base_url, directory_id_my_documents, "Восстановленная папка")
        assert_status_code(response)
        directory_id = response.json()["Id"]

        response = DocumentDirectory.delete_directory(base_url, directory_id)
        assert_status_code(response)

        response = DocumentDirectory.restore_directory(base_url, directory_id)
        assert_status_code(response)
