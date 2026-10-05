from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
resposta = client.get("/health")

def test_health_check():
    assert resposta.status_code == 200
    assert resposta.json() == {"status": "OK"}