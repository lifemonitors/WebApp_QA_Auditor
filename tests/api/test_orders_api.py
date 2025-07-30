import requests

def test_create_order():
    payload = {
        "user_id": 1,
        "items": [101, 102],
        "total": 59.99
    }
    response = requests.post("https://your-webapp.com/api/orders", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data.get("order_id") is not None
    assert data.get("status") == "created"
