# Arkhé Finance

Prazer, sou o Thiago, calouro na faculdade e esse é meu segundo projeto pessoal.

Sempre tive dificuldade de saber pra onde meu dinheiro ia no fim do mês. Pensei: por que não criar algo simples pra registrar isso do meu jeito? Foi daí que surgiu o Arkhé Finance.

---

## Sobre o projeto

Aplicação de controle financeiro pessoal rodando no terminal. Desenvolvida em Python com banco de dados SQLite3, sem dependências externas.

Feito com o que estou aprendendo agora:

- `if / elif / else`
- loop `while`
- funções com `def`
- banco de dados com `sqlite3`
- consultas SQL (`SELECT`, `INSERT`, `JOIN`)
- separação de responsabilidades em módulos

Nada além do que eu sei explicar.

---

## Como rodar

```bash
git clone https://github.com/ThiagoMateus7/Arkh--Finance
cd Arkh--Finance
python main.py
```

---

## Funcionalidades

- Registrar entradas e saídas com categoria e data
- Filtrar transações por tipo
- Calcular saldo automaticamente
- Criar categorias personalizadas
- Excluir registros pelo ID
- Validação de data e valor na entrada

---

## Estrutura

```
main.py        # menu e navegação
financas.py    # funções de negócio
database.py    # banco, tabelas e categorias padrão
```

---

## Próximos passos

**Refatoração**
- [x] Separar banco, regras e menu em arquivos distintos
- [ ] Validar se a categoria escolhida combina com o tipo da transação

**Funcionalidades**
- [ ] Filtrar transações por período
- [ ] Exportar dados em `.csv`
- [ ] Relatório de gastos por categoria

---

## Changelog

### v1.1 — Refatoração
- Separação do código em três arquivos (`main.py`, `financas.py`, `database.py`)
- Adicionado `PRAGMA foreign_keys` e `CHECK` no schema do banco
- Validação de data com `datetime.strptime`
- Bloqueio de valor `<= 0` e descrição vazia
- Padronização dos valores internos sem acento (`saida`, `entrada`)

### v1.0 — Primeira versão
- Registro de entradas e saídas com categoria e data
- Listagem com filtro por tipo
- Cálculo de saldo
- Categorias padrão e customizáveis
- Exclusão por ID

---

> *"Be water my friend."* — Bruce Lee

Feito por [Thiago Mateus](https://github.com/ThiagoMateus7)
