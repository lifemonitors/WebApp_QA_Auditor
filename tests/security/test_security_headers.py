import requests
import pytest

REQUIRED_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Access-Control-Allow-Origin"
]

@pytest.mark.parametrize("url", [
    "https://example.com",
    "https://httpbin.org"
])
def test_security_headers(url):
    response = requests.get(url)
    headers = response.headers

    for header in REQUIRED_HEADERS:
        assert header in headers, f"Missing security header: {header}"
