import urllib
from api.DocumentDirectory_api import DocumentDirectory
from assertion import assert_status_code


class TestRenameDirectory:
    def test_rename_directory(self, base_url, directory_id_my_documents):
        # создание каталога, переименование каталога
        response = DocumentDirectory.create_directory(base_url, directory_id_my_documents, "Папка")
        assert_status_code(response)
        directory_id = response.json()["Id"]

        new_name = "Новое_название"
        encoded_new_name = urllib.parse.quote(new_name, encoding='utf-8')

        response = DocumentDirectory.rename_directory(base_url, directory_id, encoded_new_name)
        assert_status_code(response)
        assert response.json()["Id"] == directory_id
        assert response.json()["Name"] == new_name
