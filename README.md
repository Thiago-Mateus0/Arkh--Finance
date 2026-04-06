# Arkhé Finance API

Prazer, sou o Thiago, estudante de Ciência da Computação, e esse é um dos meus projetos com foco em backend.

Depois de desenvolver uma aplicação de controle financeiro, quis evoluir a ideia para uma API REST, organizando melhor a lógica da aplicação e praticando conceitos mais próximos do desenvolvimento backend.

---

## Sobre o projeto

API de controle financeiro pessoal desenvolvida com Python, FastAPI e SQLite.

A proposta do projeto é permitir o gerenciamento de transações financeiras, categorias e um resumo geral dos dados, mantendo uma estrutura simples, organizada e fácil de entender.

Feito com o que estou aprendendo agora:

- rotas com FastAPI
- operações CRUD
- banco de dados com SQLite
- query parameters para filtros
- organização de responsabilidades em módulos
- estrutura inicial de uma API REST

Nada além do que eu consigo explicar com clareza.

---

## Como rodar

```
git clone https://github.com/Thiago-Mateus0/arkhe-finance-api
cd arkhe-finance-api

python3 -m venv venv
source venv/bin/activate

pip install fastapi uvicorn
uvicorn main:app --reload

```

## A aplicação ficará disponível em:
```
http://127.0.0.1:8000

http://127.0.0.1:8000/docs
```
## Funcionalidades
```
Registrar transações de entrada e saída
```
```
Listar transações cadastradas
```
```
Atualizar transações por ID
```
```
Deletar transações
```
```
Filtrar transações por tipo
```
```
Filtrar transações por categoria
```
```
Filtrar transações por intervalo de datas
```
```
Criar e remover categorias
```
```
Visualizar resumo financeiro no dashboard
```

## Estrutura
```
app/
├── database.py
└── routes/
    ├── categorias.py
    ├── dashboard.py
    └── transacoes.py

main.py
Endpoints principais
Transações
GET /transacoes
POST /transacoes
PUT /transacoes/{id}
DELETE /transacoes/{id}
```
## Filtros disponíveis:
```
?tipo=entrada
?categoria_id=1
?data_inicio=YYYY-MM-DD&data_fim=YYYY-MM-DD
Categorias
GET /categorias
POST /categorias
DELETE /categorias/{id}
Dashboard
GET /dashboard
Próximos passos
```

## Estrutura
```
 Separar schemas com Pydantic
 Criar uma camada de services
 Melhorar a organização interna da aplicação
```

## Funcionalidades

 Adicionar autenticação
 Implementar paginação
 Expandir os filtros das rotas

## Qualidade

 Adicionar testes automatizados
 Melhorar o tratamento de erros
 Fazer deploy da API
 
## Changelog
```
v1.0 — Primeira versão
CRUD de transações
CRUD de categorias
Filtros por tipo, categoria e data
Dashboard com resumo financeiro
```
```
"Be water, my friend." — Bruce Lee
```
Feito por Thiago Mateus
