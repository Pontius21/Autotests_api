
from api.Documents_api import Documents
from assertion import assert_status_code


class TestCreateDocuments:
    def test_create_document(self, directory_id_my_documents):
        # создание документа
        response = Documents.create_document(directory_id_my_documents, "Документ.docx")
        assert_status_code(response)

    def test_create_table(self, directory_id_my_documents):
        # создание таблицы
        response = Documents.create_table(directory_id_my_documents, "Таблица.xlsx")
        assert_status_code(response)

    def test_create_presentation(self, directory_id_my_documents):
        # создание презентации
        response = Documents.create_presentation(directory_id_my_documents, "Презентация.pptx")
        assert_status_code(response)
