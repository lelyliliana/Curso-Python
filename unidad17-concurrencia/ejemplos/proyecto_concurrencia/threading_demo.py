"""Demostración de concurrencia para tareas I/O-bound simuladas."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from time import perf_counter, sleep


def procesar_tarea(nombre: str, espera: float = 0.02) -> str:
    """Simula una espera breve y devuelve un resultado."""
    sleep(espera)
    return f"{nombre} completada"


def ejecutar_secuencial(nombres: list[str]) -> list[str]:
    return [procesar_tarea(nombre) for nombre in nombres]


def ejecutar_con_threads(nombres: list[str]) -> list[str]:
    with ThreadPoolExecutor(max_workers=3) as executor:
        return list(executor.map(procesar_tarea, nombres))


def ejecutar_segun_finalizacion(nombres: list[str]) -> list[str]:
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(procesar_tarea, nombre) for nombre in nombres]
        return [future.result() for future in as_completed(futures)]


def main() -> None:
    nombres = ["tarea 1", "tarea 2", "tarea 3"]
    inicio = perf_counter()
    print(ejecutar_secuencial(nombres))
    print(f"Secuencial: {perf_counter() - inicio:.4f} s")

    inicio = perf_counter()
    print(ejecutar_con_threads(nombres))
    print(f"Threads: {perf_counter() - inicio:.4f} s")


if __name__ == "__main__":
    main()
