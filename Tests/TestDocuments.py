from api.Documents_api import Documents


class TestDocuments:

    def test_create_delete_doc(self):
        response = Documents.create_doc()
        assert response.status_code == 200, "Ошибка создания документа. Код состояния ответа не является успешным"
        id_doc = response.json()[0]["Id"]

        response = Documents.delete(id_doc)
        assert response.status_code == 200, "Ошибка удаления документа. Код состояния ответа не является успешным"


    def test_create_delete_tab(self):
        response = Documents.create_tab()
        assert response.status_code == 200, "Ошибка создания таблицы. Код состояния ответа не является успешным"
        id_doc = response.json()[0]["Id"]

        response = Documents.delete(id_doc)
        assert response.status_code == 200, "Ошибка удаления таблицы. Код состояния ответа не является успешным"
