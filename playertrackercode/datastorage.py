import sqlite3

class PlayerDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT
        )''')
        self.conn.commit()

    def add_player(self, name):
        self.cursor.execute("INSERT INTO players (name) VALUES (?)", (name,))
        self.conn.commit()

    def get_players(self):
        self.cursor.execute("SELECT * FROM players")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
