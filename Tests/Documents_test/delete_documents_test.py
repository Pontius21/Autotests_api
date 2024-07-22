
from api.Documents_api import Documents
from assertion import assert_status_code


class TestDeleteDocuments:
    def test_delete_document(self, base_url, directory_id_my_documents):
        # создание документа, удаление документа
        response = Documents.create_document(base_url, directory_id_my_documents, "Документ.docx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = Documents.delete(base_url, [document_id])
        assert_status_code(response)

    def test_delete_table(self, base_url, directory_id_my_documents):
        # создание таблицы, удаление таблицы
        response = Documents.create_table(base_url, directory_id_my_documents, "Таблица.xlsx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = Documents.delete(base_url, [document_id])
        assert_status_code(response)

    def test_delete_presentation(self, base_url, directory_id_my_documents):
        # создание презентации, удаление презентации
        response = Documents.create_presentation(base_url, directory_id_my_documents, "Презентация.pptx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = Documents.delete(base_url, [document_id])
        assert_status_code(response)

    def test_multiple_delete_document(self, base_url, directory_id_my_documents):
        # создание документов, множественное удаление документов
        response = Documents.create_document(base_url, directory_id_my_documents, "Документ1.docx")
        assert_status_code(response)
        document1_id = response.json()[0]["Id"]

        response = Documents.create_document(base_url, directory_id_my_documents, "Документ2.docx")
        assert_status_code(response)
        document2_id = response.json()[0]["Id"]

        response = Documents.delete(base_url, [document1_id, document2_id])
        assert_status_code(response)