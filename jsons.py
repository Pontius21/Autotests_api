import configparser

parser = configparser.ConfigParser()
parser.read('config.ini')
id_my_documents = parser.get('config', 'id_my_documents')


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
    def for_create_document(document_name):
        json = {
            "DirectoryId": id_my_documents,
            "Name": document_name,
            "MimeType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        }
        return json

    @staticmethod
    def for_create_table(table_name):
        json = {
            "DirectoryId": id_my_documents,
            "Name": table_name,
            "MimeType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        }
        return json

    @staticmethod
    def for_create_presentation(presentation_name):
        json = {
            "DirectoryId": id_my_documents,
            "Name": presentation_name,
            "MimeType": "application/vnd.openxmlformats-officedocument.presentationml.presentation"
        }
        return json

    @staticmethod
    def for_create_directory(directory_name):
        json = {
            "Name": directory_name,
            "Description": "temp",
            "Order": 100,
            "Type": "Default",
            "IconId": None,
            "RoleIds": [],
            "UserIds": [],
            "ParentId": id_my_documents
        }
        return json

    @staticmethod
    def for_delete(document_id):
        json = {
            "Ids": document_id  # список для документов, целое число для папок
        }
        return json

    @staticmethod
    def for_upload():
        json = {
            'DirectoryId': f'{id_my_documents}'
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
