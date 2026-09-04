"""Esquemas Pydantic de entrada y salida de la API."""

from pydantic import BaseModel, Field


class EstudianteCrear(BaseModel):
    nombre: str = Field(min_length=1)
    edad: int = Field(ge=0)
    programa: str = Field(min_length=1)


class EstudianteActualizar(BaseModel):
    nombre: str | None = Field(default=None, min_length=1)
    edad: int | None = Field(default=None, ge=0)
    programa: str | None = Field(default=None, min_length=1)


class EstudianteRespuesta(BaseModel):
    id: int
    nombre: str
    edad: int
    programa: str
