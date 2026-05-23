import logging
import os
from fastapi import HTTPException
from groq import Groq
from models import Response


def get_logger():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger("fastapi")


def common_api_token(api_token: str):
    logger = get_logger()
    API_TOKEN = os.getenv("API_TOKEN")
    logger.info(f"Verificando token: {api_token}")
    if api_token != API_TOKEN:
        logger.warning(f"Token inválido: {api_token}")
        raise HTTPException(status_code=401, detail="Token inválido")
    logger.info("Token válido")
    return {"api_token": api_token}


def executar_prompt(prompt: str, model: str = "llama-3.1-8b-instant") -> Response:
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )
    return Response(value=chat_completion.choices[0].message.content)
