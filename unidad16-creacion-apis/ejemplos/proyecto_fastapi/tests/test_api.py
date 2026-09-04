"""Pruebas locales de la API mediante TestClient."""

import pytest
from fastapi.testclient import TestClient

from app.main import app, repositorio


@pytest.fixture(autouse=True)
def repositorio_limpio() -> None:
    repositorio.reset()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def crear_estudiante(client: TestClient) -> dict[str, object]:
    response = client.post(
        "/estudiantes",
        json={"nombre": "Ana", "edad": 20, "programa": "Sistemas"},
    )
    assert response.status_code == 201
    return response.json()


def test_inicio(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "API Académica disponible"}


def test_lista_inicial_vacia(client: TestClient) -> None:
    assert client.get("/estudiantes").json() == []


def test_crear_estudiante(client: TestClient) -> None:
    datos = crear_estudiante(client)
    assert datos == {"id": 1, "nombre": "Ana", "edad": 20, "programa": "Sistemas"}


def test_obtener_estudiante(client: TestClient) -> None:
    creado = crear_estudiante(client)
    response = client.get(f"/estudiantes/{creado['id']}")
    assert response.status_code == 200
    assert response.json() == creado


def test_estudiante_inexistente_devuelve_404(client: TestClient) -> None:
    response = client.get("/estudiantes/999")
    assert response.status_code == 404


def test_body_invalido_devuelve_error_validacion(client: TestClient) -> None:
    response = client.post(
        "/estudiantes",
        json={"nombre": "Ana", "edad": -1, "programa": "Sistemas"},
    )
    assert response.status_code == 422


def test_filtrar_por_programa(client: TestClient) -> None:
    crear_estudiante(client)
    response = client.get("/estudiantes", params={"programa": "Sistemas"})
    assert len(response.json()) == 1


def test_patch_actualiza_solo_campos_enviados(client: TestClient) -> None:
    creado = crear_estudiante(client)
    response = client.patch(f"/estudiantes/{creado['id']}", json={"edad": 21})
    assert response.status_code == 200
    assert response.json()["edad"] == 21
    assert response.json()["nombre"] == "Ana"


def test_delete_devuelve_204_sin_cuerpo(client: TestClient) -> None:
    creado = crear_estudiante(client)
    response = client.delete(f"/estudiantes/{creado['id']}")
    assert response.status_code == 204
    assert response.content == b""
    assert client.get(f"/estudiantes/{creado['id']}").status_code == 404


def test_estado_no_se_comparte_entre_pruebas(client: TestClient) -> None:
    assert client.get("/estudiantes").json() == []
