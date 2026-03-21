from datetime import datetime
from database import conn, cursor


def hoje():
    return datetime.now().strftime("%Y-%m-%d")


def data_valida(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def mostrar_categorias(tipo):
    categorias = cursor.execute(
        "SELECT id, nome FROM categorias WHERE tipo = ? OR tipo = 'ambos'",
        (tipo,)
    ).fetchall()
    print("\nCategorias:")
    for cat in categorias:
        print(f"  {cat[0]}. {cat[1]}")
    return categorias


def registrar_transacao(tipo):
    print("\n-- Nova", "entrada" if tipo == "entrada" else "saida", "--")

    try:
        valor = float(input("Valor (R$): ").replace(",", "."))
        if valor <= 0:
            print("O valor precisa ser maior que zero.")
            return
    except ValueError:
        print("Valor inválido.")
        return

    descricao = input("Descrição: ").strip()
    if descricao == "":
        descricao = "Sem descrição"

    data = input("Data (AAAA-MM-DD) ou Enter pra hoje: ").strip()
    if data == "":
        data = hoje()
    elif not data_valida(data):
        print("Data inválida. Use o formato AAAA-MM-DD.")
        return

    mostrar_categorias(tipo)

    try:
        cat_id = int(input("Número da categoria: "))
    except ValueError:
        print("Categoria inválida.")
        return

    cursor.execute(
        "INSERT INTO transacoes (tipo, valor, descricao, categoria_id, data) VALUES (?, ?, ?, ?, ?)",
        (tipo, valor, descricao, cat_id, data)
    )
    conn.commit()
    print("Registrado!")


def ver_transacoes():
    print("\n1. Todas  2. Entradas  3. Saídas")
    opcao = input("Opção: ")

    filtros = {"1": "", "2": "WHERE t.tipo = 'entrada'", "3": "WHERE t.tipo = 'saida'"}

    if opcao not in filtros:
        print("Opção inválida.")
        return

    rows = cursor.execute(f"""
        SELECT t.id, t.data, t.tipo, c.nome, t.valor, t.descricao
        FROM transacoes t
        JOIN categorias c ON c.id = t.categoria_id
        {filtros[opcao]}
        ORDER BY t.data DESC
    """).fetchall()

    if len(rows) == 0:
        print("Nenhuma transação encontrada.")
        return

    print()
    for r in rows:
        sinal = "+" if r[2] == "entrada" else "-"
        print(f"[{r[0]}] {r[1]}  {r[3]:<15} {sinal}R$ {r[4]:.2f}  ({r[5]})")

    # calcula o saldo geral (não filtrado, mas tá bom por enquanto)
    entrada = cursor.execute("SELECT SUM(valor) FROM transacoes WHERE tipo = 'entrada'").fetchone()[0] or 0
    saida = cursor.execute("SELECT SUM(valor) FROM transacoes WHERE tipo = 'saida'").fetchone()[0] or 0
    print(f"\nEntradas: R$ {entrada:.2f} | Saídas: R$ {saida:.2f} | Saldo: R$ {entrada - saida:.2f}")


def excluir_transacao():
    try:
        tid = int(input("ID da transação: "))
    except ValueError:
        print("ID inválido.")
        return

    row = cursor.execute("SELECT id FROM transacoes WHERE id = ?", (tid,)).fetchone()
    if row is None:
        print("Não encontrada.")
        return

    cursor.execute("DELETE FROM transacoes WHERE id = ?", (tid,))
    conn.commit()
    print("Excluída.")


def nova_categoria():
    nome = input("Nome da categoria: ").strip()
    if nome == "":
        print("O nome não pode ser vazio.")
        return

    print("Tipo: 1=entrada  2=saida  3=ambos")
    opcao = input("Opção: ")

    if opcao == "1":
        tipo = "entrada"
    elif opcao == "2":
        tipo = "saida"
    elif opcao == "3":
        tipo = "ambos"
    else:
        print("Opção inválida.")
        return

    cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", (nome, tipo))
    conn.commit()
    print("Categoria criada!")
