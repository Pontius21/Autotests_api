from api.DocumentDirectory_api import DocumentDirectory
from assertion import assert_status_code


class TestDownloadDirectory:
    def test_download_directory(self, base_url, directory_id_my_documents):
        # создание каталога и скачивание каталога
        response = DocumentDirectory.create_directory(base_url, directory_id_my_documents, "Папка")
        directory_id = response.json()["Id"]

        response = DocumentDirectory.archive_directory(base_url, directory_id)
        assert_status_code(response)
