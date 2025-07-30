import requests

def test_xss_vulnerability():
    payload = "<script>alert('XSS')</script>"
    params = {"q": payload}
    response = requests.get("https://your-webapp.com/search", params=params)
    assert payload not in response.text, "Potential XSS vulnerability detected"
