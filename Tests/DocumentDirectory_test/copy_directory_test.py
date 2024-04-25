from api.DocumentDirectory_api import DocumentDirectory
from assertion import assert_status_code


class TestCopyDirectory:
    def test_copy_directory(self):
        # создание папок, копирование одной папки в другую, удаление папок
        response = DocumentDirectory.create_directory("Папка1")
        directory1_id = response.json()["Id"]

        response = DocumentDirectory.create_directory("Папка2")
        directory2_id = response.json()["Id"]

        response = DocumentDirectory.copy_directory(directory1_id, directory2_id)
        assert_status_code(response)

        response = DocumentDirectory.delete_directory(directory1_id)
        assert_status_code(response)

        response = DocumentDirectory.delete_directory(directory2_id)
        assert_status_code(response)