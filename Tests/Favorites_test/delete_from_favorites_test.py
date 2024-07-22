from api.Documents_api import Documents
from api.Favorites_api import Favorites
from assertion import assert_status_code


class TestDeleteFavorites:
    def test_delete_from_favorites(self,base_url, directory_id_my_documents):
        # создание документа, добавление документа в избранное, удаление документа из избранного
        response = Documents.create_document(base_url, directory_id_my_documents, "Документ.docx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = Favorites.add_to_favorites(base_url, document_id)
        assert_status_code(response)

        response = Favorites.delete_from_favorites(base_url, document_id)
        assert_status_code(response)
