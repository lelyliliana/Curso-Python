"""Demostración de concurrencia cooperativa con asyncio."""

import asyncio


async def procesar_tarea(nombre: str, espera: float = 0.01) -> str:
    """Simula I/O asíncrono y devuelve un resultado."""
    await asyncio.sleep(espera)
    return f"{nombre} completada"


async def ejecutar_varias(nombres: list[str]) -> list[str]:
    tareas = [asyncio.create_task(procesar_tarea(nombre)) for nombre in nombres]
    return list(await asyncio.gather(*tareas))


async def tarea_con_error() -> None:
    await asyncio.sleep(0)
    raise ValueError("Error simulado")


async def main() -> None:
    resultados = await ejecutar_varias(["tarea 1", "tarea 2", "tarea 3"])
    print(resultados)


if __name__ == "__main__":
    asyncio.run(main())
