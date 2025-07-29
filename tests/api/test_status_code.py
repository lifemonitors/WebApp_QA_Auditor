import requests

def test_homepage_status():
    response = requests.get("https://www.saucedemo.com")
    assert response.status_code == 200
