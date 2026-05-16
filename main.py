from enum import Enum

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

API_TOKEN = "1234567890abcdef"


def common_api_token(api_token: str):
    if api_token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido")
    return {"api_token": api_token}


app = FastAPI(
    title="Aula",
    description="API desenvolvida durante a aula de Construção de APIs para IA",
    summary="API desenvolvida durante a aula de Construção de APIs para IA",
    version="0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Kellerman Paulo da Mota",
        "url": "http://github.com/kellerman.paulo/",
        "email": "kellerman.paulo@ufg.br",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    dependencies=[Depends(common_api_token)],
)


class Numeros(BaseModel):
    numero1: int
    numero2: int


class TipoOperacao(str, Enum):
    soma = "soma"
    subtracao = "subtracao"
    multiplicacao = "multiplicacao"
    divisao = "divisao"


class Response(BaseModel):
    value: float


@app.post("/operacao_matematica")
def operacao_matematica(numeros: Numeros, operacao: TipoOperacao):
    if operacao == TipoOperacao.soma:
        return Response(value=numeros.numero1 + numeros.numero2)
    elif operacao == TipoOperacao.subtracao:
        return Response(value=numeros.numero1 - numeros.numero2)
    elif operacao == TipoOperacao.multiplicacao:
        return Response(value=numeros.numero1 * numeros.numero2)
    elif operacao == TipoOperacao.divisao:
        return Response(value=numeros.numero1 / numeros.numero2)


@app.get("/teste")
def hello_world():
    return {"mensagem": " Hello World"}


# Passando o número 1 e 2 na URL
@app.get(
    path="/soma/{numero1}/{numero2}",
    summary="Soma dois números inteiros",
    description="Recebe dois números inteiros e retorna a soma",
    tags=["Operações matemáticas"],
    status_code=200,
)
def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


# Passando o número 1 e 2 no corpo da requisição
@app.post("/soma_formato2", tags=["Operações matemáticas"])
def soma_formato2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


@app.post(
    "/soma_formato3",
    tags=["Operações matemáticas"],
)
def soma_formato3(numeros: Numeros):
    if numeros.api_token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido")

    total = numeros.numero1 + numeros.numero2
    if numeros.numero1 < 0:
        raise HTTPException(
            status_code=400, detail="Número 1 deve ser maior ou igual a zero"
        )
    return {"resultado": total}
