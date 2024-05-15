from api.DocumentDirectory_api import DocumentDirectory
from assertion import assert_status_code


class TestDownloadDirectory:
    def test_download_directory(self):
        # создание каталога, скачивание каталога и удаление каталога
        response = DocumentDirectory.create_directory("Папка")
        directory_id = response.json()["Id"]

        response = DocumentDirectory.archive_directory(directory_id)
        assert_status_code(response)

        response = DocumentDirectory.delete_directory(directory_id)
        assert_status_code(response)