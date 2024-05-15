from api.DocumentDirectory_api import DocumentDirectory
from api.Documents_api import Documents
from assertion import assert_status_code


class TestMoveDocument:
    def test_move_document(self):
        # создание документа и папки, перемещение документа в папку, удаление папки
        response = Documents.create_document("Документ.docx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = DocumentDirectory.create_directory("Папка")
        assert_status_code(response)
        directory_id = response.json()["Id"]

        response = Documents.move_document(document_id, directory_id)
        assert_status_code(response)

        response = DocumentDirectory.delete_directory(directory_id)
        assert_status_code(response)