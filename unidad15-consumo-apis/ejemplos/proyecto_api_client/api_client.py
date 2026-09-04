"""Cliente HTTP síncrono para una API académica hipotética."""

from types import TracebackType
from typing import Any

import requests

from modelos import Estudiante


class APIClient:
    """Centraliza las solicitudes HTTP hacia la API académica."""

    def __init__(
        self,
        base_url: str,
        timeout: float = 10.0,
        session: requests.Session | None = None,
    ) -> None:
        if timeout <= 0:
            raise ValueError("El timeout debe ser positivo")
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._session = session or requests.Session()
        self._owns_session = session is None
        self._session.headers.update({"Accept": "application/json"})

    def close(self) -> None:
        """Cierra la sesión creada internamente por el cliente."""
        if self._owns_session:
            self._session.close()

    def __enter__(self) -> "APIClient":
        return self

    def __exit__(
        self,
        tipo_error: type[BaseException] | None,
        valor_error: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()

    def _request(
        self,
        metodo: str,
        ruta: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        permitir_404: bool = False,
    ) -> requests.Response:
        url = f"{self.base_url}/{ruta.lstrip('/')}"
        response = self._session.request(
            metodo,
            url,
            params=params,
            json=json,
            timeout=self.timeout,
        )
        if not (permitir_404 and response.status_code == 404):
            response.raise_for_status()
        return response

    def listar_estudiantes(
        self,
        *,
        pagina: int = 1,
        limite: int = 10,
        programa: str | None = None,
    ) -> list[Estudiante]:
        """Obtiene una página de estudiantes, con filtro opcional."""
        params: dict[str, Any] = {"pagina": pagina, "limite": limite}
        if programa is not None:
            params["programa"] = programa
        response = self._request("GET", "/estudiantes", params=params)
        datos = response.json()
        if not isinstance(datos, list):
            raise ValueError("Se esperaba una lista de estudiantes")
        return [Estudiante.desde_dict(elemento) for elemento in datos]

    def obtener_estudiante(self, estudiante_id: int) -> Estudiante | None:
        """Obtiene un estudiante o devuelve None para un 404."""
        response = self._request(
            "GET",
            f"/estudiantes/{estudiante_id}",
            permitir_404=True,
        )
        if response.status_code == 404:
            return None
        datos = response.json()
        if not isinstance(datos, dict):
            raise ValueError("Se esperaba un objeto de estudiante")
        return Estudiante.desde_dict(datos)

    def crear_estudiante(self, datos: dict[str, Any]) -> Estudiante:
        """Crea un estudiante mediante POST."""
        response = self._request("POST", "/estudiantes", json=datos)
        respuesta = response.json()
        if not isinstance(respuesta, dict):
            raise ValueError("Se esperaba el estudiante creado")
        return Estudiante.desde_dict(respuesta)

    def actualizar_estudiante(
        self,
        estudiante_id: int,
        cambios: dict[str, Any],
    ) -> Estudiante:
        """Actualiza parcialmente un estudiante mediante PATCH."""
        response = self._request(
            "PATCH",
            f"/estudiantes/{estudiante_id}",
            json=cambios,
        )
        datos = response.json()
        if not isinstance(datos, dict):
            raise ValueError("Se esperaba el estudiante actualizado")
        return Estudiante.desde_dict(datos)

    def eliminar_estudiante(self, estudiante_id: int) -> None:
        """Elimina un estudiante; un 204 exitoso no tiene JSON."""
        self._request("DELETE", f"/estudiantes/{estudiante_id}")
