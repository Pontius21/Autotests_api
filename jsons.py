class JSONS:

    @staticmethod
    def for_login(login, password):
        json = {
            "Login": login,
            "Password": password,
            "DeviceId": "F26A5A0C-8824-4F13-B4AB-835CF4CFBCAC"
        }
        return json

    @staticmethod
    def for_create_doc():
        json = {
            "DirectoryId": 1,
            "Name": "empty.docx",
            "MimeType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        }
        return json

    @staticmethod
    def for_create_tab():
        json = {
            "DirectoryId": 1,
            "Name": "empty.xlsx",
            "MimeType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        }
        return json

    @staticmethod
    def for_delete(id_doc):
        json = {
            "Ids": [id_doc]
        }
        return json
