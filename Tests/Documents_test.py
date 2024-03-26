import urllib

import pytest

from api.DocumentDirectory_api import DocumentDirectory
from api.Documents_api import Documents


class TestDocuments:

    def test_create_delete_document(self):
        # создание и удаление документа
        response = Documents.create_document("Документ.docx")
        assert response.status_code == 200, "Ошибка создания документа"
        document_id = response.json()[0]["Id"]

        response = Documents.delete([document_id])
        assert response.status_code == 200, "Ошибка удаления документа"


    def test_create_delete_table(self):
        # создание и удаление таблицы
        response = Documents.create_table("Таблица.xlsx")
        assert response.status_code == 200, "Ошибка создания таблицы"
        document_id = response.json()[0]["Id"]

        response = Documents.delete([document_id])
        assert response.status_code == 200, "Ошибка удаления таблицы"

    def test_create_delete_presentation(self):
        # создание и удаление презентации
        response = Documents.create_presentation("Презентация.pptx")
        assert response.status_code == 200, "Ошибка создания презентации"
        document_id = response.json()[0]["Id"]

        response = Documents.delete([document_id])
        assert response.status_code == 200, "Ошибка удаления презентации"

    @pytest.mark.parametrize("document_name", ['Test DOCX.docx', '1341831.jpg'])
    def test_upload_file(self, document_name):
        # загрузка документа/изображения в "Мои документы" и удаление документа/изображения
        response = Documents.upload(document_name)
        assert response.status_code == 200, f"Ошибка загрузки файла: {response.json()['ErrorMessage']}"
        document_id = response.json()[0]["Id"]

        response = Documents.delete([document_id])
        assert response.status_code == 200, "Ошибка удаления файла"

    def test_move_document(self):
        # создание документа и папки, перемещение документа в папку, удаление папки
        response = Documents.create_document("Документ.docx")
        document_id = response.json()[0]["Id"]

        response = DocumentDirectory.create_directory("Папка")
        directory_id = response.json()["Id"]

        response = Documents.move_document(document_id, directory_id)
        assert response.status_code == 200, "Ошибка перемещения документа"

        response = DocumentDirectory.delete_directory(directory_id)
        assert response.status_code == 200, "Ошибка удаления папки"

    def test_copy_document(self):
        # создание документа и папки, копирование документа в папку, удаление папки и документа
        response = Documents.create_document("Документ.docx")
        document_id = response.json()[0]["Id"]

        response = DocumentDirectory.create_directory("Папка")
        directory_id = response.json()["Id"]

        response = Documents.copy_document(document_id, directory_id)
        assert response.status_code == 200, "Ошибка копирования документа"

        response = DocumentDirectory.delete_directory(directory_id)
        assert response.status_code == 200, "Ошибка удаления папки"

        response = Documents.delete([document_id])
        assert response.status_code == 200, "Ошибка удаления документа"

    def test_download_document(self):
        # создание документа, скачивание документа, удаление документа
        response = Documents.create_document("Документ.docx")
        document_id = response.json()[0]["Id"]

        response = Documents.download_document(document_id)
        assert response.status_code == 200, f"Ошибка скачивания документа: {response.json()['ErrorMessage']}"

        Documents.delete([document_id])

    def test_rename_document(self):
        # создание документа, переименование документа, удаление документа
        response = Documents.create_document("Документ.docx")
        document_id = response.json()[0]["Id"]

        new_name = "Новое_название.docx"
        encoded_new_name = urllib.parse.quote(new_name, encoding='utf-8')

        response = Documents.rename_document(document_id, encoded_new_name)
        assert response.status_code == 200
        assert response.json()["Id"] == document_id
        assert response.json()["Name"] == new_name

        Documents.delete([document_id])

