"""Demostración pequeña de trabajo CPU-bound con procesos."""

from concurrent.futures import ProcessPoolExecutor


def sumar_cuadrados(limite: int) -> int:
    """Suma los cuadrados desde cero hasta limite - 1."""
    return sum(numero * numero for numero in range(limite))


def ejecutar_secuencial(limites: list[int]) -> list[int]:
    return [sumar_cuadrados(limite) for limite in limites]


def ejecutar_con_procesos(limites: list[int]) -> list[int]:
    """Distribuye cálculos entre procesos y conserva el orden de entrada."""
    with ProcessPoolExecutor() as executor:
        return list(executor.map(sumar_cuadrados, limites))


def main() -> None:
    limites = [10_000, 12_000, 14_000]
    print("Secuencial:", ejecutar_secuencial(limites))
    print("Procesos:", ejecutar_con_procesos(limites))


if __name__ == "__main__":
    main()
