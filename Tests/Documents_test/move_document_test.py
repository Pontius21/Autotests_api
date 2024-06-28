from api.DocumentDirectory_api import DocumentDirectory
from api.Documents_api import Documents
from assertion import assert_status_code


class TestMoveDocument:
    def test_move_document(self, directory_id_my_documents):
        # создание документа и каталога, перемещение документа в каталог
        response = Documents.create_document(directory_id_my_documents, "Документ.docx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = DocumentDirectory.create_directory(directory_id_my_documents, "Папка")
        assert_status_code(response)
        directory_id = response.json()["Id"]

        response = Documents.move_document(document_id, directory_id)
        assert_status_code(response)