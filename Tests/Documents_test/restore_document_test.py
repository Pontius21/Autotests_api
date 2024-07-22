
from api.Documents_api import Documents
from assertion import assert_status_code


class TestRestoreDocument:
    def test_restore_document(self, base_url, directory_id_my_documents):
        # создание документа, удаление документа, восстановление документа
        response = Documents.create_document(base_url, directory_id_my_documents, "восстановление.docx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = Documents.delete(base_url, [document_id])
        assert_status_code(response)

        response = Documents.restore_document(base_url, document_id)
        assert_status_code(response)