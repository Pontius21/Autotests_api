from api.DocumentDirectory_api import DocumentDirectory
from api.Documents_api import Documents
from assertion import assert_status_code


class TestDirectoryGet:
    def test_directory_get(self):
        # Получение списка с основными директориями
        response = DocumentDirectory.directory_get()
        assert_status_code(response)

    def test_sort(self):
        # создание документов и каталогов, сортировка по названию (по возрастанию и убыванию), удаление каталогов и
        # множественное удаление документов
        document1_name = "Документ1.docx"
        document2_name = "Документ2.docx"
        directory1_name = "Папка1"
        directory2_name = "Папка2"

        response = Documents.create_document(document1_name)
        assert_status_code(response)
        document1_id = response.json()[0]["Id"]

        response = Documents.create_document(document2_name)
        assert_status_code(response)
        document2_id = response.json()[0]["Id"]

        response = DocumentDirectory.create_directory(directory1_name)
        assert_status_code(response)
        directory1_id = response.json()["Id"]

        response = DocumentDirectory.create_directory(directory2_name)
        assert_status_code(response)
        directory2_id = response.json()["Id"]

        response = DocumentDirectory.sort(542, 1, 0)
        assert_status_code(response)

        assert response.json()[0]["Children"][0]["Name"] == directory1_name
        assert response.json()[0]["Children"][0]["Id"] == directory1_id

        assert response.json()[0]["Children"][1]["Name"] == directory2_name
        assert response.json()[0]["Children"][1]["Id"] == directory2_id

        assert response.json()[0]["Documents"][0]["Name"] == document1_name
        assert response.json()[0]["Documents"][0]["Id"] == document1_id

        assert response.json()[0]["Documents"][1]["Name"] == document2_name
        assert response.json()[0]["Documents"][1]["Id"] == document2_id

        response = DocumentDirectory.sort(542, 1, 1)
        assert_status_code(response)

        assert response.json()[0]["Children"][0]["Name"] == directory2_name
        assert response.json()[0]["Children"][0]["Id"] == directory2_id

        assert response.json()[0]["Children"][1]["Name"] == directory1_name
        assert response.json()[0]["Children"][1]["Id"] == directory1_id

        assert response.json()[0]["Documents"][0]["Name"] == document2_name
        assert response.json()[0]["Documents"][0]["Id"] == document2_id

        assert response.json()[0]["Documents"][1]["Name"] == document1_name
        assert response.json()[0]["Documents"][1]["Id"] == document1_id

        response = DocumentDirectory.delete_directory(directory1_id)
        assert_status_code(response)
        response = DocumentDirectory.delete_directory(directory2_id)
        assert_status_code(response)

        response = Documents.delete([document1_id, document2_id])
        assert_status_code(response)