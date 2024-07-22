import urllib
from api.DocumentDirectory_api import DocumentDirectory
from api.Documents_api import Documents
from assertion import assert_status_code


class TestSearch:
    def test_search_document(self, base_url, directory_id_my_documents):
        # создание документов, поиск существующего документа, поиск несуществующего документа
        document1_name = "поиск1.docx"
        document2_name = "поиск2.docx"

        response = Documents.create_document(base_url, directory_id_my_documents, document1_name)
        assert_status_code(response)

        response = Documents.create_document(base_url, directory_id_my_documents, document2_name)
        assert_status_code(response)

        search_text = document2_name
        encoded_search_text = urllib.parse.quote(search_text, encoding='utf-8')

        response = DocumentDirectory.search(base_url, encoded_search_text)
        assert_status_code(response)
        assert response.json()["Document"]["Items"][0]["Name"] == document2_name

        search_text = "поиск14245245.docx"
        encoded_search_text = urllib.parse.quote(search_text, encoding='utf-8')

        response = DocumentDirectory.search(base_url, encoded_search_text)
        assert_status_code(response)
        assert response.json()["Document"]["Items"] == []

    def test_search_directory(self, base_url, directory_id_my_documents):
        # создание каталогов, поиск существующего каталога, поиск несуществующего каталога
        directory1_name = "папка11"
        directory2_name = "папка22"

        response = DocumentDirectory.create_directory(base_url, directory_id_my_documents, directory1_name)
        assert_status_code(response)

        response = DocumentDirectory.create_directory(base_url, directory_id_my_documents, directory2_name)
        assert_status_code(response)

        search_text = directory2_name
        encoded_search_text = urllib.parse.quote(search_text, encoding='utf-8')

        response = DocumentDirectory.search(base_url, encoded_search_text)
        assert_status_code(response)
        assert response.json()["Directory"]["Items"][0]["Name"] == directory2_name

        search_text = "папка14245245"
        encoded_search_text = urllib.parse.quote(search_text, encoding='utf-8')

        response = DocumentDirectory.search(base_url, encoded_search_text)
        assert_status_code(response)
        assert response.json()["Directory"]["Items"] == []