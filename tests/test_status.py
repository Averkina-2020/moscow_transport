from fastapi.testclient import TestClient

from moscow_transport.main import app

client = TestClient(app)


def test_metro_news():
    days = '2'
    result = client.get('metro/news', params={'days': days})
    assert result.status_code == 200
