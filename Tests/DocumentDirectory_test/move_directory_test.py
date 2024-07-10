
from api.DocumentDirectory_api import DocumentDirectory
from assertion import assert_status_code


class TestMoveDirectory:
    def test_move_directory(self, directory_id_my_documents):
        # создание каталогов, перемещение одного каталога в другой
        response = DocumentDirectory.create_directory(directory_id_my_documents, "Папка1")
        assert_status_code(response)
        directory1_id = response.json()["Id"]

        response = DocumentDirectory.create_directory(directory_id_my_documents, "Папка2")
        assert_status_code(response)
        directory2_id = response.json()["Id"]

        response = DocumentDirectory.move_directory(directory1_id, directory2_id)
        assert_status_code(response)
