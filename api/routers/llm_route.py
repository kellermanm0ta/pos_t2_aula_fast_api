from fastapi import APIRouter
from models import Historia
from utils import executar_prompt

router = APIRouter()


@router.post("/gerar_historia")
def gerar_historia(historia: Historia):
    prompt = f"Escreva uma história sobre {historia.tema}"
    return executar_prompt(prompt)
