import os
import mysql.connector


class Database:

    def connect(self):
        return mysql.connector.connect(
            host=os.getenv("DB_HOST", "db"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME", "educafuturo"),
            connection_timeout=300,
            charset="utf8mb4" # <-- ADICIONE ESTA LINHA AQUI
        )

    def query(self, sql, valores=None):
        conn = self.connect()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(sql, valores or ())
        resultado = cursor.fetchall()

        cursor.close()
        conn.close()

        return resultado

    def execute(self, sql, valores=None):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(sql, valores or ())
        conn.commit()

        ultimo_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return ultimo_id