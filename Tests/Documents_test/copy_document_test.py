from api.DocumentDirectory_api import DocumentDirectory
from api.Documents_api import Documents
from assertion import assert_status_code


class TestCopyDocument:
    def test_copy_document(self):
        # создание документа и папки, копирование документа в папку, удаление папки и документа
        response = Documents.create_document("Документ.docx")
        document_id = response.json()[0]["Id"]

        response = DocumentDirectory.create_directory("Папка")
        directory_id = response.json()["Id"]

        response = Documents.copy_document(document_id, directory_id)
        assert_status_code(response)

        response = DocumentDirectory.delete_directory(directory_id)
        assert_status_code(response)

        response = Documents.delete([document_id])
        assert_status_code(response)