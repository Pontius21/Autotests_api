
def assert_status_code(response, code=200):
    assert response.status_code == code,\
        f"Ожидался status_code = {code}, получен status_code = {response.status_code}. " \
        f"ErrorMessage: {response.json()['ErrorMessage']} "

