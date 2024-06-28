from api.Documents_api import Documents
from assertion import assert_status_code


class TestDownloadDocument:
    def test_download_document(self, directory_id_my_documents):
        # создание документа, скачивание документа
        response = Documents.create_document(directory_id_my_documents, "Документ.docx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = Documents.download_document(document_id)
        assert_status_code(response)
