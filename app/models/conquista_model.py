from database.db import Database

class ConquistaModel:

    def __init__(self):
        self.db = Database()

    # =========================
    # TODAS AS CONQUISTAS
    # =========================
    def listar_todas(self):

        return self.db.query("""
            SELECT *
            FROM conquistas
            ORDER BY id
        """)

    # =========================
    # CONQUISTAS DO USUÁRIO
    # =========================
    def listar_usuario(self, user_id):

        return self.db.query("""
            SELECT conquista_id
            FROM user_conquistas
            WHERE user_id = %s
        """, (user_id,))

    # =========================
    # ADICIONAR CONQUISTA
    # =========================
    def adicionar_conquista(self, user_id, conquista_id):

        self.db.execute("""
            INSERT IGNORE INTO user_conquistas
            (user_id, conquista_id)
            VALUES (%s,%s)
        """, (
            user_id,
            conquista_id
        ))

    # =========================
    # TOTAL DE AULAS
    # =========================
    def total_aulas(self, user_id):

        res = self.db.query("""
            SELECT COUNT(DISTINCT aula_id) total
            FROM progresso
            WHERE user_id = %s
            AND concluido = 1
        """, (user_id,))

        return res[0]["total"] if res else 0

    # =========================
    # XP
    # =========================
    def total_xp(self, user_id):

        res = self.db.query("""
            SELECT xp
            FROM aluno_stats
            WHERE user_id = %s
        """, (user_id,))

        return res[0]["xp"] if res else 0