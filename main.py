from enum import Enum
import os
from typing import Any

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
import logging
from dotenv import load_dotenv

from groq import Groq

load_dotenv()  # Loads variables from .env into os.environ

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("fastapi")

API_TOKEN = "123"


def common_api_token(api_token: str):
    logger.info(f"Verificando token: {api_token}")
    if api_token != API_TOKEN:
        logger.warning(f"Token inválido: {api_token}")
        raise HTTPException(status_code=401, detail="Token inválido")
    logger.info("Token válido")
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
    value: Any


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


class Historia(BaseModel):
    tema: str


@app.post("/gerar_historia")
def gerar_historia(historia: Historia):
    prompt = f"Escreva uma história sobre {historia.tema}"
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant",
    )
    return Response(value=chat_completion.choices[0].message.content)
