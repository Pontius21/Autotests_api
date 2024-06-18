
from api.Documents_api import Documents
from assertion import assert_status_code


class TestCreateDocuments:
    def test_create_document(self):
        # создание документа
        response = Documents.create_document("Документ.docx")
        assert_status_code(response)

    def test_create_table(self):
        # создание таблицы
        response = Documents.create_table("Таблица.xlsx")
        assert_status_code(response)

    def test_create_presentation(self):
        # создание презентации
        response = Documents.create_presentation("Презентация.pptx")
        assert_status_code(response)
