from api.DocumentDirectory_api import DocumentDirectory
from assertion import assert_status_code


class TestCopyDirectory:
    def test_copy_directory(self, base_url, directory_id_my_documents):
        # создание каталогов, копирование одного каталога в другой
        response = DocumentDirectory.create_directory(base_url, directory_id_my_documents, "Папка1")
        assert_status_code(response)
        directory1_id = response.json()["Id"]

        response = DocumentDirectory.create_directory(base_url, directory_id_my_documents, "Папка2")
        assert_status_code(response)
        directory2_id = response.json()["Id"]

        response = DocumentDirectory.copy_directory(base_url, directory1_id, directory2_id)
        assert_status_code(response)
