import urllib
from api.DocumentDirectory_api import DocumentDirectory
from api.Documents_api import Documents
from assertion import assert_status_code


class TestSearch:
    def test_search_document(self):
        # создание документов, поиск существующего документа, поиск несуществующего документа,
        # множественное удаление документов
        document1_name = "поиск1.docx"
        document2_name = "поиск2.docx"

        response = Documents.create_document(document1_name)
        assert_status_code(response)
        document1_id = response.json()[0]["Id"]

        response = Documents.create_document(document2_name)
        document2_id = response.json()[0]["Id"]

        search_text = document2_name
        encoded_search_text = urllib.parse.quote(search_text, encoding='utf-8')

        response = DocumentDirectory.search(encoded_search_text)
        assert_status_code(response)
        assert response.json()["Document"]["Items"][0]["Name"] == document2_name

        search_text = "поиск14245245.docx"
        encoded_search_text = urllib.parse.quote(search_text, encoding='utf-8')

        response = DocumentDirectory.search(encoded_search_text)
        assert_status_code(response)
        assert response.json()["Document"]["Items"] == []

        Documents.delete([document1_id, document2_id])

    def test_search_directory(self):
        # создание каталогов, поиск существующего каталога, поиск несуществующего каталога, удаление каталогов
        directory1_name = "папка11"
        directory2_name = "папка22"

        response = DocumentDirectory.create_directory(directory1_name)
        directory1_id = response.json()["Id"]

        response = DocumentDirectory.create_directory(directory2_name)
        directory2_id = response.json()["Id"]

        search_text = directory2_name
        encoded_search_text = urllib.parse.quote(search_text, encoding='utf-8')

        response = DocumentDirectory.search(encoded_search_text)
        assert_status_code(response)
        assert response.json()["Directory"]["Items"][0]["Name"] == directory2_name

        search_text = "папка14245245"
        encoded_search_text = urllib.parse.quote(search_text, encoding='utf-8')

        response = DocumentDirectory.search(encoded_search_text)
        assert_status_code(response)
        assert response.json()["Directory"]["Items"] == []

        DocumentDirectory.delete_directory(directory1_id)
        DocumentDirectory.delete_directory(directory2_id)