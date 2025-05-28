import mysql.connector
from config import Config

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASS,
            database=Config.DB_NAME
        )
        self.cursor = self.conn.cursor(prepared=True)

    def insert_user(self, name, email, encrypted_info):
        sql = "INSERT INTO users (name, email, info) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (name, email, encrypted_info))
        self.conn.commit()

    def fetch_users(self):
        sql = "SELECT id, name, email FROM users"
        self.cursor.execute(sql)
        return self.cursor.fetchall()