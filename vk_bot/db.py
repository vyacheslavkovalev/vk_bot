import sqlite3

from model import User


class Database:
    def __init__(self, db_file: str):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id: int):
        with self.connection:
            result = self.cursor.execute(f'SELECT * FROM Users WHERE user_id = {user_id}').fetchone()
        return bool(len(result))

    def add_user(self, user: User):
        with self.connection:
            return self.cursor.execute(f'INSERT INTO Users (user_id, first_name, last_name) VALUES ({user.user_id}, {user.first_name}, {user.last_name})')

    def delete_user(self, user_id):
        with self.connection:
            return self.cursor.execute(f'DELETE FROM Users WHERE user_id = {user_id}')

    def get_ids(self):
        with self.connection:
            return [t[0] for t in self.cursor.execute('SELECT user_id FROM Users').fetchall()]
