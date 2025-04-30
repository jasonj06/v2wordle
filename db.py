from flask import g
import sqlite3

def connect_db():
    con = sqlite3.connect('guesses.db')
    con.row_factory = sqlite3.Row

    con.set_trace_callback(print)
    return con

def get_db():
    if not hasattr(g, 'sqlite.db'):
        g.sqlite_db = connect_db()

    return g.sqlite_db

def create_tables():
    db = get_db()
    db.execute("""CREATE TABLE IF NOT EXISTS guesses(
                    id INTEGER PRIMARY KEY,
                    guess TEXT
                );""")
    
    db.commit()