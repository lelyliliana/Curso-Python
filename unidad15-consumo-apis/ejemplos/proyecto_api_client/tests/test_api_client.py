"""Pruebas del cliente API; ninguna realiza solicitudes de red."""

from unittest.mock import Mock

import pytest
import requests

from api_client import APIClient
from modelos import Estudiante


@pytest.fixture
def session() -> Mock:
    session = Mock(spec=requests.Session)
    session.headers = {}
    return session


@pytest.fixture
def cliente(session: Mock) -> APIClient:
    return APIClient("https://api.ejemplo.com/", timeout=3.0, session=session)


def crear_response(
    datos: object = None,
    *,
    status_code: int = 200,
) -> Mock:
    response = Mock(spec=requests.Response)
    response.status_code = status_code
    response.json.return_value = datos
    response.raise_for_status.return_value = None
    return response


def test_normalizar_base_url(session: Mock) -> None:
    cliente = APIClient("https://api.ejemplo.com///", session=session)

    assert cliente.base_url == "https://api.ejemplo.com"


def test_listar_estudiantes_usa_get_url_params_y_timeout(
    cliente: APIClient,
    session: Mock,
) -> None:
    session.request.return_value = crear_response(
        [{"id": 1, "nombre": "Ana", "edad": 20, "programa": "Sistemas"}]
    )

    estudiantes = cliente.listar_estudiantes(
        pagina=2,
        limite=5,
        programa="Sistemas",
    )

    assert estudiantes == [Estudiante(1, "Ana", 20, "Sistemas")]
    session.request.assert_called_once_with(
        "GET",
        "https://api.ejemplo.com/estudiantes",
        params={"pagina": 2, "limite": 5, "programa": "Sistemas"},
        json=None,
        timeout=3.0,
    )


def test_obtener_estudiante_por_id(cliente: APIClient, session: Mock) -> None:
    session.request.return_value = crear_response(
        {"id": 7, "nombre": "Luis", "edad": 22, "programa": "Ingeniería"}
    )

    estudiante = cliente.obtener_estudiante(7)

    assert estudiante == Estudiante(7, "Luis", 22, "Ingeniería")
    session.request.assert_called_once_with(
        "GET",
        "https://api.ejemplo.com/estudiantes/7",
        params=None,
        json=None,
        timeout=3.0,
    )


def test_obtener_estudiante_404_devuelve_none(
    cliente: APIClient,
    session: Mock,
) -> None:
    response = crear_response(status_code=404)
    session.request.return_value = response

    assert cliente.obtener_estudiante(999) is None
    response.raise_for_status.assert_not_called()


def test_crear_estudiante_envia_json(cliente: APIClient, session: Mock) -> None:
    entrada = {"nombre": "Ana", "edad": 20, "programa": "Sistemas"}
    session.request.return_value = crear_response({"id": 1, **entrada}, status_code=201)

    creado = cliente.crear_estudiante(entrada)

    assert creado.id == 1
    session.request.assert_called_once_with(
        "POST",
        "https://api.ejemplo.com/estudiantes",
        params=None,
        json=entrada,
        timeout=3.0,
    )


def test_actualizar_estudiante_usa_patch(cliente: APIClient, session: Mock) -> None:
    session.request.return_value = crear_response(
        {"id": 1, "nombre": "Ana", "edad": 21, "programa": "Sistemas"}
    )

    actualizado = cliente.actualizar_estudiante(1, {"edad": 21})

    assert actualizado.edad == 21
    assert session.request.call_args.args == (
        "PATCH",
        "https://api.ejemplo.com/estudiantes/1",
    )
    assert session.request.call_args.kwargs["json"] == {"edad": 21}


def test_eliminar_204_no_intenta_leer_json(
    cliente: APIClient,
    session: Mock,
) -> None:
    response = crear_response(status_code=204)
    session.request.return_value = response

    resultado = cliente.eliminar_estudiante(1)

    assert resultado is None
    response.raise_for_status.assert_called_once_with()
    response.json.assert_not_called()


def test_error_http_se_propaga(cliente: APIClient, session: Mock) -> None:
    response = crear_response()
    response.raise_for_status.side_effect = requests.HTTPError("Error 500")
    session.request.return_value = response

    with pytest.raises(requests.HTTPError, match="500"):
        cliente.listar_estudiantes()


def test_timeout_se_propaga_sin_espera_real(
    cliente: APIClient,
    session: Mock,
) -> None:
    session.request.side_effect = requests.Timeout("Tiempo agotado")

    with pytest.raises(requests.Timeout, match="agotado"):
        cliente.listar_estudiantes()


def test_respuesta_de_lista_con_formato_invalido(
    cliente: APIClient,
    session: Mock,
) -> None:
    session.request.return_value = crear_response({"resultado": []})

    with pytest.raises(ValueError, match="lista"):
        cliente.listar_estudiantes()


def test_desde_dict_valida_campos_faltantes() -> None:
    with pytest.raises(ValueError, match="Faltan campos"):
        Estudiante.desde_dict({"id": 1, "nombre": "Ana"})


def test_cliente_cierra_session_creada_internamente(monkeypatch: pytest.MonkeyPatch) -> None:
    session_interna = Mock(spec=requests.Session)
    session_interna.headers = {}
    monkeypatch.setattr(requests, "Session", Mock(return_value=session_interna))

    with APIClient("https://api.ejemplo.com"):
        pass

    session_interna.close.assert_called_once_with()
