from pydantic import BaseModel
from enum import Enum
from typing import Any


class Numeros(BaseModel):
    numero1: int
    numero2: int


class TipoOperacao(str, Enum):
    soma = "soma"
    subtracao = "subtracao"
    multiplicacao = "multiplicacao"
    divisao = "divisao"


class Response(BaseModel):
    value: Any


class Historia(BaseModel):
    tema: str
