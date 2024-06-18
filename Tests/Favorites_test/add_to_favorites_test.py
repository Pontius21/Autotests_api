from api.Documents_api import Documents
from api.Favorites_api import Favorites
from assertion import assert_status_code


class TestAddFavorites:
    def test_add_to_favorites(self):
        # создание документа, добавление документа в избранное
        response = Documents.create_document("Избранное.docx")
        assert_status_code(response)
        document_id = response.json()[0]["Id"]

        response = Favorites.add_to_favorites(document_id)
        assert_status_code(response)
