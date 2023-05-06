from app import app
def test_HTTP():
    response = app.test_client.get('/')
    assert response.status_code == 200