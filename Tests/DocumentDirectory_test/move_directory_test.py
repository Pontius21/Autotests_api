from api.DocumentDirectory_api import DocumentDirectory
from assertion import assert_status_code


class TestMoveDirectory:
    def test_move_directory(self):
        # создание папок, перемещение одной папки в другую, удаление папки
        response = DocumentDirectory.create_directory("Папка1")
        assert_status_code(response)
        directory1_id = response.json()["Id"]

        response = DocumentDirectory.create_directory("Папка2")
        assert_status_code(response)
        directory2_id = response.json()["Id"]

        response = DocumentDirectory.move_directory(directory1_id, directory2_id)
        assert_status_code(response)

        response = DocumentDirectory.delete_directory(directory2_id)
        assert_status_code(response)