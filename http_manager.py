import requests


class HttpManager:
    auth_token = ""

    @staticmethod
    def auth(url, body):
        response = requests.post(url, json=body)
        HttpManager.auth_token = response.headers['Set-Cookie']
        return response

    @staticmethod
    def get(url):
        response = requests.get(url, headers={'Cookie': HttpManager.auth_token})
        return response

    @staticmethod
    def post(url, body):
        response = requests.post(url, json=body, headers={'Cookie': HttpManager.auth_token})
        return response

    @staticmethod
    def delete(url):
        response = requests.delete(url, headers={'Cookie': HttpManager.auth_token})
        return response
