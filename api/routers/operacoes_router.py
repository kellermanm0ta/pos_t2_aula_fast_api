from fastapi import APIRouter
from models import TipoOperacao, Numeros, Response
from utils import API_TOKEN
from fastapi import HTTPException

router = APIRouter()


@router.post("/operacao_matematica")
def operacao_matematica(numeros: Numeros, operacao: TipoOperacao):
    if operacao == TipoOperacao.soma:
        return Response(value=numeros.numero1 + numeros.numero2)
    elif operacao == TipoOperacao.subtracao:
        return Response(value=numeros.numero1 - numeros.numero2)
    elif operacao == TipoOperacao.multiplicacao:
        return Response(value=numeros.numero1 * numeros.numero2)
    elif operacao == TipoOperacao.divisao:
        return Response(value=numeros.numero1 / numeros.numero2)


# Passando o número 1 e 2 na URL
@router.get(
    path="/soma/{numero1}/{numero2}",
    summary="Soma dois números inteiros",
    description="Recebe dois números inteiros e retorna a soma",
    status_code=200,
)
def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


# Passando o número 1 e 2 no corpo da requisição
@router.post("/soma_formato2")
def soma_formato2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


@router.post(
    "/soma_formato3",
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
