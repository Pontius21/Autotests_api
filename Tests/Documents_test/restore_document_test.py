import time
from api.Documents_api import Documents
from assertion import assert_status_code


class TestRestoreDocument:
    def test_restore_document(self):
        # создание документа, удаление документа, восстановление документа, удаление документа
        response = Documents.create_document("восстановление.docx")
        document_id = response.json()[0]["Id"]

        Documents.delete([document_id])

        response = Documents.restore_document(document_id)
        assert_status_code(response)

        time.sleep(5)
        Documents.delete([document_id])