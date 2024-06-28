

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
    def for_create_document(directory_id, document_name):
        json = {
            "DirectoryId": directory_id,
            "Name": document_name,
            "MimeType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        }
        return json

    @staticmethod
    def for_create_table(directory_id, table_name):
        json = {
            "DirectoryId": directory_id,
            "Name": table_name,
            "MimeType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        }
        return json

    @staticmethod
    def for_create_presentation(directory_id, presentation_name):
        json = {
            "DirectoryId": directory_id,
            "Name": presentation_name,
            "MimeType": "application/vnd.openxmlformats-officedocument.presentationml.presentation"
        }
        return json

    @staticmethod
    def for_create_directory(directory_id, directory_name):
        json = {
            "Name": directory_name,
            "Description": "temp",
            "Order": 100,
            "Type": "Default",
            "IconId": None,
            "RoleIds": [],
            "UserIds": [],
            "ParentId": directory_id
        }
        return json

    @staticmethod
    def for_delete(document_id):
        json = {
            "Ids": document_id  # список для документов, целое число для папок
        }
        return json

    @staticmethod
    def for_upload(directory_id):
        json = {
            'DirectoryId': f'{directory_id}'
        }
        return json

    @staticmethod
    def for_upload_file(file_name):
        files = {
            'file': open(f'upload_source/{file_name}', 'rb')
        }
        return files

    @staticmethod
    def for_move(ids, to_directory_id):
        json = {
            'Ids': [ids],
            'ToDirectoryId': to_directory_id
        }
        return json

    @staticmethod
    def for_favorites(document_id):
        json = {
            'EntityIds': [document_id],
            'Type': "Document"
        }
        return json

    @staticmethod
    def for_restore(ids):
        json = {
            'Ids': [ids]
        }
        return json
