from api.Documents_api import Documents
from assertion import assert_status_code


class TestDownloadDocument:
    def test_download_document(self):
        # создание документа, скачивание документа, удаление документа
        response = Documents.create_document("Документ.docx")
        document_id = response.json()[0]["Id"]

        response = Documents.download_document(document_id)
        assert_status_code(response)

        Documents.delete([document_id])