from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_ci():
    response = client.post("/cis/", json={
        "nombre_ci": "App1",
        "tipo_ci": "Software",
        "estado_actual": "Activo"
    })
    assert response.status_code == 200
    assert response.json()["nombre_ci"] == "App1"
