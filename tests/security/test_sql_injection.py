import requests

def test_sql_injection():
    payload = "' OR '1'='1"
    params = {"username": payload, "password": "anything"}
    response = requests.post("https://your-webapp.com/login", data=params)
    assert "invalid" in response.text.lower() or response.status_code == 401, "Potential SQL Injection vulnerability"
