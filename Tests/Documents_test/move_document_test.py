from api.DocumentDirectory_api import DocumentDirectory
from api.Documents_api import Documents
from assertion import assert_status_code


class TestMoveDocument:
    def test_move_document(self, base_url, directory_id_my_documents):
        # создание документа и каталога, перемещение документа в каталог
        response = Documents.create_document(base_url, directory_id_my_documents, "Документ.docx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = DocumentDirectory.create_directory(base_url, directory_id_my_documents, "Папка")
        assert_status_code(response)
        directory_id = response.json()["Id"]

        response = Documents.move_document(base_url, document_id, directory_id)
        assert_status_code(response)