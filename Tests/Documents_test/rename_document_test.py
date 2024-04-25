import urllib
from api.Documents_api import Documents
from assertion import assert_status_code


class TestRenameDocument:
    def test_rename_document(self):
        # создание документа, переименование документа, удаление документа
        response = Documents.create_document("Документ.docx")
        document_id = response.json()[0]["Id"]

        new_name = "Новое_название.docx"
        encoded_new_name = urllib.parse.quote(new_name, encoding='utf-8')

        response = Documents.rename_document(document_id, encoded_new_name)
        assert_status_code(response)
        assert response.json()["Id"] == document_id
        assert response.json()["Name"] == new_name

        Documents.delete([document_id])