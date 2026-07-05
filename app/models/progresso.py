from database.db import Database

class Progresso:

    def __init__(self):
        self.db = Database()

    def salvar_teoria(self, user_id, aula_id):
        self.db.execute("""
            INSERT INTO progresso (user_id, aula_id, teoria)
            VALUES (%s,%s,1)
            ON DUPLICATE KEY UPDATE teoria=1
        """, (user_id, aula_id))

    def salvar_pratica(self, user_id, aula_id):
        self.db.execute("""
            UPDATE progresso
            SET pratica=1
            WHERE user_id=%s AND aula_id=%s
        """, (user_id, aula_id))

    def salvar_atividade(self, user_id, aula_id, acertos, total):

        aprovado = acertos >= 7

        self.db.execute("""
            UPDATE progresso
            SET atividade=1,
                acertos=%s,
                total=%s,
                aprovado=%s,
                concluido=%s,
                data_conclusao=NOW()
            WHERE user_id=%s AND aula_id=%s
        """, (acertos, total, aprovado, aprovado, user_id, aula_id))

    def buscar_progresso(self, user_id, aula_id):
        return self.db.query("""
            SELECT *
            FROM progresso
            WHERE user_id=%s AND aula_id=%s
        """, (user_id, aula_id))