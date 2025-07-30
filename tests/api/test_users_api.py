import requests

def test_get_user_details():
    response = requests.get("https://your-webapp.com/api/users/1")
    assert response.status_code == 200
    data = response.json()
    assert "username" in data
    assert "email" in data
