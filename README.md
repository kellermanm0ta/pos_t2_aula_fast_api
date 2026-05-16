# pos_t2_aula_fast_api

## Descrição

Projeto Python com FastAPI que implementa uma API para operações matemáticas simples. A API utiliza autenticação por token para proteger os endpoints.

## Funcionalidades

- Token de acesso: `1234567890abcdef`
- Modelo Pydantic `Numeros` com os campos `numero1` e `numero2`
- Enum `TipoOperacao` para definir as operações matemáticas suportadas

## Endpoints

- `POST /operacao_matematica`
  - Recebe um corpo JSON com `numero1`, `numero2` e o parâmetro de consulta `operacao`
  - Operações suportadas: `soma`, `subtracao`, `multiplicacao`, `divisao`
  - Retorna um objeto JSON com `value`

- `GET /soma/{numero1}/{numero2}`
  - Soma dois inteiros passados na URL
  - Retorna `{"resultado": total}`

- `POST /soma_formato2`
  - Soma dois inteiros passados no corpo da requisição como parâmetros simples
  - Retorna `{"resultado": total}`

- `POST /soma_formato3`
  - Soma dois números passados no corpo da requisição usando o modelo `Numeros`
  - Valida `numero1 >= 0`
  - Retorna `{"resultado": total}`

- `GET /teste`
  - Retorna `{"mensagem": " Hello World"}`

## Requisitos

- Python >= 3.12
- Dependências definidas em `pyproject.toml`

## Dependências

- `fastapi[standard] >= 0.136.1`
