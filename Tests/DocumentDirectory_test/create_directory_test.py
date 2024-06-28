from api.DocumentDirectory_api import DocumentDirectory
from assertion import assert_status_code


class TestCreateDirectory:
    def test_create_directory(self, directory_id_my_documents):
        # создание каталога
        response = DocumentDirectory.create_directory(directory_id_my_documents, "Папка")
        assert_status_code(response)
