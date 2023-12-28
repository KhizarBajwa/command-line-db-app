# database.py

import sqlite3

class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def fetch_all(self, table):
        query = f"SELECT * FROM {table}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def insert_user(self, name, email):
        query = f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')"
        self.execute_query(query)

    def update_user_email(self, user_id, new_email):
        query = f"UPDATE users SET email = '{new_email}' WHERE id = {user_id}"
        self.execute_query(query)

    def delete_user(self, user_id):
        query = f"DELETE FROM users WHERE id = {user_id}"
        self.execute_query(query)
