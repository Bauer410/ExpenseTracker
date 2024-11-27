from unittest.mock import patch

from app import function_to_test, app
import pytest


@pytest.fixture
def client():
    app.debug = True
    client = app.test_client()
    yield client


@patch('app.session', {})
def test_index_not_logged_in(client):
    response = client.get("/")
    html = response.data.decode()

    assert "You should be redirected" in html
    assert response.location == "/login"
    assert response.status_code == 302


# !!! DUE TO THE DATABASE USAGE IT DOES NOT WORK, A MOCKING DATABASE IS REQUIRED !!!
# @patch('app.session', {'username': 'test'})
# def test_index_logged_in(client):
#     response = client.get(follow_redirects=True)
#     html = response.data.decode()
#
#     assert "Expense Tracker" in html
#     assert response.status_code == 200


# !!! DUE TO THE DATABASE USAGE IT DOES NOT WORK, A MOCKING DATABASE IS REQUIRED !!!
# def test_login_failure(client):
#     response = client.post('/loginVerify', data={
#         'username': 'test',
#         'password': 'password_wrong'
#     }, follow_redirects=True)
#     html = response.data.decode()
#
#     assert "Invalid credentials" in html
#     assert response.status_code == 200


# !!! DUE TO THE DATABASE USAGE IT DOES NOT WORK, A MOCKING DATABASE IS REQUIRED !!!
# def test_login_success(client):
#     response = client.post('/loginVerify', data={
#         'username': 'test',
#         'password': 'password'
#     }, follow_redirects=True)
#     html = response.data.decode()
#
#     assert "Expense Tracker" in html
#     assert response.status_code == 200


def test_functionToTest():
    assert 16 == function_to_test(4)
