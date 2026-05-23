# pos_t2_aula_fast_api

## Descrição

API em FastAPI desenvolvida durante a disciplina — fornece endpoints para operações matemáticas e integração com um provedor LLM (via `groq`). O código principal está em [api/main.py](api/main.py).

## Estrutura principal

- **api/main.py**: Instancia a aplicação FastAPI e registra os routers.
- **api/routers/operacoes_router.py**: Endpoints para operações matemáticas.
- **api/routers/llm_route.py**: Endpoint para gerar textos com o LLM.
- **api/models.py**: Modelos Pydantic utilizados nas requisições/respostas.
- **api/utils.py**: Helpers (logging, verificação de token e integração com Groq).

## Variáveis de ambiente

- **API_TOKEN**: token esperado pela API (verificado globalmente via Dependência em `api/main.py`).
- **GROQ_API_KEY**: chave para acessar o serviço Groq (usado em `utils.executar_prompt`).

Coloque as variáveis em um arquivo `.env` na raiz do projeto ou exporte no ambiente. Veja [env.sample](env.sample) como exemplo.

## Requisitos

- Python >= 3.12
- Dependências em `pyproject.toml` (instalação abaixo).

## Instalação

1. Criar e ativar um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instalar o pacote e dependências:

```bash
pip install -e .
```

## Executando a API

Inicie o servidor com `uvicorn` apontando para o app em `api.main`:

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

OBS: Todos os endpoints estão protegidos pela dependência `common_api_token`, portanto inclua o parâmetro de consulta `api_token` em suas requisições (ex.: `?api_token=SEU_TOKEN`).

## Endpoints principais

- `POST /gerar_historia` — gera uma história via LLM.
  - Corpo: `{ "tema": "texto" }`
  - Retorna: `Response` com `value` contendo o texto gerado.

- `POST /operacao_matematica` — realiza operação entre dois números.
  - Corpo: `{ "numero1": int, "numero2": int }`
  - Parâmetro de consulta: `operacao` (valores: `soma`, `subtracao`, `multiplicacao`, `divisao`).
  - Retorna: `{ "value": resultado }`

- `GET /soma/{numero1}/{numero2}` — soma dois inteiros passados na URL. Retorna `{ "resultado": total }`.

- `POST /soma_formato2` — soma dois inteiros recebidos como parâmetros simples no corpo da requisição.

- `POST /soma_formato3` — soma usando o modelo `Numeros` (validações aplicadas no endpoint).

Nota: a verificação global de `API_TOKEN` exige que cada requisição contenha `api_token` como parâmetro de consulta, por exemplo:

```bash
curl -X GET "http://localhost:8000/soma/2/3?api_token=SEU_TOKEN"
```

E exemplo de chamada ao LLM:

```bash
curl -X POST "http://localhost:8000/gerar_historia?api_token=SEU_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"tema":"um dragão curioso"}'
```

## Observações

- A integração com o Groq exige `GROQ_API_KEY` válida.
- Veja `api/utils.py` para detalhes da implementação do cliente Groq e do logger.
- Se quiser, posso também corrigir pequenas inconsistências no código (por exemplo, `soma_formato3` tenta ler `numeros.api_token` mas o modelo `Numeros` não define esse campo). Deseja que eu ajuste isso agora?
