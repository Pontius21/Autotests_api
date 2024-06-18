from api.DocumentDirectory_api import DocumentDirectory
from api.Documents_api import Documents
from assertion import assert_status_code


class TestCopyDocument:
    def test_copy_document(self):
        # создание документа и папки, копирование документа в папку
        response = Documents.create_document("Документ.docx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = DocumentDirectory.create_directory("Папка")
        assert_status_code(response)
        directory_id = response.json()["Id"]

        response = Documents.copy_document(document_id, directory_id)
        assert_status_code(response)
