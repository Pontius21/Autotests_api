import pytest

from api.Documents_api import Documents
from assertion import assert_status_code


class TestUpload:
    @pytest.mark.parametrize("document_name", ['Test DOCX.docx', '1341831.jpg'])
    def test_upload_file(self, document_name):
        # загрузка документа/изображения в "Мои документы" и удаление документа/изображения
        response = Documents.upload(document_name)
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = Documents.delete([document_id])
        assert_status_code(response)
