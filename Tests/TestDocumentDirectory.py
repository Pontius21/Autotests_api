from api.DocumentDirectory_api import DocumentDirectory


class TestDocumentDirectory:

    def test_directory_get(self):
        response = DocumentDirectory.directory_get()
        assert response.status_code == 200

