from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    resposta = client.get("/health")
    assert resposta.status_code == 200
    assert resposta.json() == {"status": "OK"}