import sqlite3


conn = sqlite3.connect('book_manager.db')
cursor = conn.cursor()

def create_table_book():
    cursor.execute("""CREATE TABLE IF NOT EXISTS book(
                   book_id TEXT PRIMARY KEY,
                   name TEXT NOT NULL,
                   finished BOOLEAN,
                   rating REAL CHECK (rating<5 AND rating>0)
                   ) """)
    conn.commit()

if __name__ == "__main__":
    create_table_book()