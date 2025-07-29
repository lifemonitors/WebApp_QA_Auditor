import requests
import pytest

@pytest.mark.parametrize("url", [
    "https://example.com",
    "https://httpbin.org/status/200"
])
def test_status_code(url):
    response = requests.get(url)
    assert response.status_code == 200
