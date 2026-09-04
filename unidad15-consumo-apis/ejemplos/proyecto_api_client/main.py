"""Demostración manual del cliente de la API académica."""

import requests

from api_client import APIClient


def main() -> None:
    """Consulta una URL ficticia que debe sustituirse antes de ejecutar."""
    base_url = "https://api.ejemplo.com"
    try:
        with APIClient(base_url, timeout=10.0) as cliente:
            estudiantes = cliente.listar_estudiantes()
            for estudiante in estudiantes:
                print(estudiante)
    except requests.Timeout:
        print("La API tardó demasiado en responder")
    except requests.HTTPError as error:
        print(f"La API respondió con un error HTTP: {error}")
    except requests.RequestException as error:
        print(f"No fue posible comunicarse con la API: {error}")
    except ValueError as error:
        print(f"La respuesta no tiene el formato esperado: {error}")


if __name__ == "__main__":
    main()
