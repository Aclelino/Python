import sqlite3


def criar_banco():
   conn = sqlite3.connect("bando_dado.db")
   c = conn.cursor()
   c.execute("CREATE TABLE IF NOT EXISTS lembrete(id INTEGER PRIMARY KEY ,lembrete TEXT NOT NULL,hora INTEGER NOT NULL,data DATE NOT NULL)")
   conn.commit()
def criar_tabela():
