import sqlite3

conn = sqlite3.connect("financas.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS categorias (
        id   INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tipo TEXT NOT NULL CHECK(tipo IN ('entrada', 'saida', 'ambos'))
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS transacoes (
        id           INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo         TEXT NOT NULL CHECK(tipo IN ('entrada', 'saida')),
        valor        REAL NOT NULL CHECK(valor > 0),
        descricao    TEXT NOT NULL,
        categoria_id INTEGER NOT NULL REFERENCES categorias(id),
        data         TEXT NOT NULL
    )
""")

total = cursor.execute("SELECT COUNT(*) FROM categorias").fetchone()[0]
if total == 0:
    cursor.execute("INSERT INTO categorias (nome, tipo) VALUES ('Alimentação', 'saida')")
    cursor.execute("INSERT INTO categorias (nome, tipo) VALUES ('Transporte', 'saida')")
    cursor.execute("INSERT INTO categorias (nome, tipo) VALUES ('Moradia', 'saida')")
    cursor.execute("INSERT INTO categorias (nome, tipo) VALUES ('Salário', 'entrada')")
    cursor.execute("INSERT INTO categorias (nome, tipo) VALUES ('Freelance', 'entrada')")
    cursor.execute("INSERT INTO categorias (nome, tipo) VALUES ('Outros', 'ambos')")
    conn.commit()
