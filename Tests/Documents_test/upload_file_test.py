import pytest

from api.Documents_api import Documents
from assertion import assert_status_code


class TestUpload:
    @pytest.mark.parametrize("document_name", ['Test DOCX.docx', '1341831.jpg'])
    def test_upload_file(self, base_url, directory_id_my_documents, document_name):
        # загрузка документа/изображения в "Мои документы"
        response = Documents.upload(base_url, directory_id_my_documents, document_name)
        assert_status_code(response)
