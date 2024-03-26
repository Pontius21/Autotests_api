import urllib

from api.DocumentDirectory_api import DocumentDirectory
from api.Documents_api import Documents


class TestDocumentDirectory:

    def test_directory_get(self):
        # Получение списка с основными директориями
        response = DocumentDirectory.directory_get()
        assert response.status_code == 200

    def test_create_directory(self):
        # создание и удаление папки
        response = DocumentDirectory.create_directory("Папка")
        assert response.status_code == 200, "Ошибка создания папки"
        directory_id = response.json()["Id"]

        response = DocumentDirectory.delete_directory(directory_id)
        assert response.status_code == 200, "Ошибка удаления папки"

    def test_sort(self):
        # создание документов и папок, сортировка по названию (по возрастанию и убыванию), удаление папок и
        # множественное удаление документов
        document1_name = "Документ1.docx"
        document2_name = "Документ2.docx"
        directory1_name = "Папка1"
        directory2_name = "Папка2"

        response = Documents.create_document(document1_name)
        assert response.status_code == 200, response.json()['ErrorMessage']
        document1_id = response.json()[0]["Id"]

        response = Documents.create_document(document2_name)
        document2_id = response.json()[0]["Id"]

        response = DocumentDirectory.create_directory(directory1_name)
        assert response.status_code == 200
        directory1_id = response.json()["Id"]

        response = DocumentDirectory.create_directory(directory2_name)
        assert response.status_code == 200
        directory2_id = response.json()["Id"]

        response = DocumentDirectory.sort(1, 1, 0)
        assert response.status_code == 200

        assert response.json()[0]["Children"][0]["Name"] == directory1_name
        assert response.json()[0]["Children"][0]["Id"] == directory1_id

        assert response.json()[0]["Children"][1]["Name"] == directory2_name
        assert response.json()[0]["Children"][1]["Id"] == directory2_id

        assert response.json()[0]["Documents"][0]["Name"] == document1_name
        assert response.json()[0]["Documents"][0]["Id"] == document1_id

        assert response.json()[0]["Documents"][1]["Name"] == document2_name
        assert response.json()[0]["Documents"][1]["Id"] == document2_id

        response = DocumentDirectory.sort(1, 1, 1)
        assert response.status_code == 200

        assert response.json()[0]["Children"][0]["Name"] == directory2_name
        assert response.json()[0]["Children"][0]["Id"] == directory2_id

        assert response.json()[0]["Children"][1]["Name"] == directory1_name
        assert response.json()[0]["Children"][1]["Id"] == directory1_id

        assert response.json()[0]["Documents"][0]["Name"] == document2_name
        assert response.json()[0]["Documents"][0]["Id"] == document2_id

        assert response.json()[0]["Documents"][1]["Name"] == document1_name
        assert response.json()[0]["Documents"][1]["Id"] == document1_id

        DocumentDirectory.delete_directory(directory1_id)
        DocumentDirectory.delete_directory(directory2_id)

        Documents.delete([document1_id, document2_id])

    def test_search_document(self):
        # создание документов, поиск существующего документа, поиск несуществующего документа,
        # множественное удаление документов
        document1_name = "поиск1.docx"
        document2_name = "поиск2.docx"

        response = Documents.create_document(document1_name)
        assert response.status_code == 200, response.json()['ErrorMessage']
        document1_id = response.json()[0]["Id"]

        response = Documents.create_document(document2_name)
        document2_id = response.json()[0]["Id"]

        search_text = document2_name
        encoded_search_text = urllib.parse.quote(search_text, encoding='utf-8')

        response = DocumentDirectory.search(encoded_search_text)
        assert response.status_code == 200
        assert response.json()["Document"]["Items"][0]["Name"] == document2_name

        search_text = "поиск14245245.docx"
        encoded_search_text = urllib.parse.quote(search_text, encoding='utf-8')

        response = DocumentDirectory.search(encoded_search_text)
        assert response.status_code == 200
        assert response.json()["Document"]["Items"] == []

        Documents.delete([document1_id, document2_id])

    def test_search_directory(self):
        # создание папок, поиск существующей папки, поиск несуществующей папки, удаление папок
        directory1_name = "папка11"
        directory2_name = "папка22"

        response = DocumentDirectory.create_directory(directory1_name)
        directory1_id = response.json()["Id"]

        response = DocumentDirectory.create_directory(directory2_name)
        directory2_id = response.json()["Id"]

        search_text = directory2_name
        encoded_search_text = urllib.parse.quote(search_text, encoding='utf-8')

        response = DocumentDirectory.search(encoded_search_text)
        assert response.status_code == 200
        assert response.json()["Directory"]["Items"][0]["Name"] == directory2_name

        search_text = "папка14245245"
        encoded_search_text = urllib.parse.quote(search_text, encoding='utf-8')

        response = DocumentDirectory.search(encoded_search_text)
        assert response.status_code == 200
        assert response.json()["Directory"]["Items"] == []

        DocumentDirectory.delete_directory(directory1_id)
        DocumentDirectory.delete_directory(directory2_id)

    def test_move_directory(self):
        # создание папок, перемещение одной папки в другую, удаление папки
        response = DocumentDirectory.create_directory("Папка1")
        directory1_id = response.json()["Id"]

        response = DocumentDirectory.create_directory("Папка2")
        directory2_id = response.json()["Id"]

        response = DocumentDirectory.move_directory(directory1_id, directory2_id)
        assert response.status_code == 200, "Ошибка перемещения папки"

        response = DocumentDirectory.delete_directory(directory2_id)
        assert response.status_code == 200

    def test_copy_directory(self):
        # создание папок, копирование одной папки в другую, удаление папок
        response = DocumentDirectory.create_directory("Папка1")
        directory1_id = response.json()["Id"]

        response = DocumentDirectory.create_directory("Папка2")
        directory2_id = response.json()["Id"]

        response = DocumentDirectory.copy_directory(directory1_id, directory2_id)
        assert response.status_code == 200, "Ошибка копирования папки"

        response = DocumentDirectory.delete_directory(directory1_id)
        assert response.status_code == 200

        response = DocumentDirectory.delete_directory(directory2_id)
        assert response.status_code == 200

    # def test_rename_directory(self):
    #     # создание каталога, переименование каталога, удаление каталога
    #     response = DocumentDirectory.create_directory("Папка")
    #     directory_id = response.json()["Id"]
    #
    #     new_name = "Новое_название"
    #     encoded_new_name = urllib.parse.quote(new_name, encoding='utf-8')
    #
    #     response = DocumentDirectory.rename_directory(directory_id, encoded_new_name)
    #     assert response.status_code == 200
    #     assert response.json()["Id"] == directory_id
    #     assert response.json()["Name"] == new_name
    #
    #     DocumentDirectory.delete_directory(directory_id)

