"""Rutas de la API académica."""

from fastapi import FastAPI, HTTPException, Query, Response, status

from app.esquemas import EstudianteActualizar, EstudianteCrear, EstudianteRespuesta
from app.repositorio import RepositorioEstudiantes

app = FastAPI(title="API Académica", version="1.0.0")
repositorio = RepositorioEstudiantes()


@app.get("/", tags=["Sistema"])
def inicio() -> dict[str, str]:
    return {"mensaje": "API Académica disponible"}


@app.get(
    "/estudiantes",
    response_model=list[EstudianteRespuesta],
    tags=["Estudiantes"],
)
def listar_estudiantes(
    programa: str | None = None,
    limite: int = Query(default=10, ge=1, le=100),
) -> list[EstudianteRespuesta]:
    return [
        EstudianteRespuesta.model_validate(estudiante, from_attributes=True)
        for estudiante in repositorio.listar(programa=programa, limite=limite)
    ]


@app.get(
    "/estudiantes/{estudiante_id}",
    response_model=EstudianteRespuesta,
    tags=["Estudiantes"],
)
def obtener_estudiante(estudiante_id: int) -> EstudianteRespuesta:
    estudiante = repositorio.obtener(estudiante_id)
    if estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return EstudianteRespuesta.model_validate(estudiante, from_attributes=True)


@app.post(
    "/estudiantes",
    response_model=EstudianteRespuesta,
    status_code=status.HTTP_201_CREATED,
    tags=["Estudiantes"],
)
def crear_estudiante(datos: EstudianteCrear) -> EstudianteRespuesta:
    estudiante = repositorio.crear(**datos.model_dump())
    return EstudianteRespuesta.model_validate(estudiante, from_attributes=True)


@app.patch(
    "/estudiantes/{estudiante_id}",
    response_model=EstudianteRespuesta,
    tags=["Estudiantes"],
)
def actualizar_estudiante(
    estudiante_id: int,
    datos: EstudianteActualizar,
) -> EstudianteRespuesta:
    cambios = datos.model_dump(exclude_unset=True, exclude_none=True)
    estudiante = repositorio.actualizar(estudiante_id, cambios)
    if estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return EstudianteRespuesta.model_validate(estudiante, from_attributes=True)


@app.delete(
    "/estudiantes/{estudiante_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Estudiantes"],
)
def eliminar_estudiante(estudiante_id: int) -> Response:
    if not repositorio.eliminar(estudiante_id):
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
