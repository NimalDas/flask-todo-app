from app import app
def test_HTTP():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_webtxt():
    response = app.test_client().get('/home')
    assert b"Total" in response.data
    assert b"Statistics" in response.data
    assert b"Pending" in response.data
    assert b"Update" in response.data