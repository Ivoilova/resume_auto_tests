import requests
import pytest

def test_api_status():
    response = requests.get("http://books.toscrape.com/")
    assert response.status_code == 200
    assert "text/html" in response.headers["Content-Type"]