from fastapi import Depends, FastAPI
from dotenv import find_dotenv, load_dotenv
from utils import common_api_token, get_logger
from routers.llm_route import router as llm_router
from routers.operacoes_router import router as operacoes_router

load_dotenv(find_dotenv())  # Loads variables from .env into os.environ

logger = get_logger()

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

app.include_router(router=llm_router, tags=["LLM"])
app.include_router(router=operacoes_router, tags=["Operações matemáticas"])
