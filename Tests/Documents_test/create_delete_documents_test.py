
from api.Documents_api import Documents
from assertion import assert_status_code


class TestCreateDeleteDocuments:
    def test_create_delete_document(self):
        # создание и удаление документа
        response = Documents.create_document("Документ.docx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = Documents.delete([document_id])
        assert_status_code(response)

    def test_create_delete_table(self):
        # создание и удаление таблицы
        response = Documents.create_table("Таблица.xlsx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = Documents.delete([document_id])
        assert_status_code(response)

    def test_create_delete_presentation(self):
        # создание и удаление презентации
        response = Documents.create_presentation("Презентация.pptx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = Documents.delete([document_id])
        assert_status_code(response)