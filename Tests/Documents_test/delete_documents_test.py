
from api.Documents_api import Documents
from assertion import assert_status_code


class TestDeleteDocuments:
    def test_delete_document(self):
        # создание документа, удаление документа
        response = Documents.create_document("Документ.docx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = Documents.delete([document_id])
        assert_status_code(response)

    def test_delete_table(self):
        # создание таблицы, удаление таблицы
        response = Documents.create_table("Таблица.xlsx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = Documents.delete([document_id])
        assert_status_code(response)

    def test_delete_presentation(self):
        # создание презентации, удаление презентации
        response = Documents.create_presentation("Презентация.pptx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = Documents.delete([document_id])
        assert_status_code(response)

    def test_multiple_delete_document(self):
        # создание документов, множественное удаление документов
        response = Documents.create_document("Документ1.docx")
        assert_status_code(response)
        document1_id = response.json()[0]["Id"]

        response = Documents.create_document("Документ2.docx")
        assert_status_code(response)
        document2_id = response.json()[0]["Id"]

        response = Documents.delete([document1_id, document2_id])
        assert_status_code(response)