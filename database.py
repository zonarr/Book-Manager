import sqlite3


conn = sqlite3.connect('book_manager.db')
cursor = conn.cursor()

def create_table_book():
    cursor.execute("""CREATE TABLE IF NOT EXISTS book(
                   book_id TEXT PRIMARY KEY,
                   name TEXT,
                   finished BOOLEAN,
                   rating REAL) """)
    conn.commit()