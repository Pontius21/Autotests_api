import time
from api.Documents_api import Documents
from assertion import assert_status_code


class TestRestoreDocument:
    def test_restore_document(self):
        # создание документа, удаление документа, восстановление документа
        response = Documents.create_document("восстановление.docx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = Documents.delete([document_id])
        assert_status_code(response)

        response = Documents.restore_document(document_id)
        assert_status_code(response)