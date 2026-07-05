from database.db import Database

class DashboardModel:

    def __init__(self):
        self.db = Database()

    def ensure_stats(self, user_id):
        self.db.execute("""
            INSERT IGNORE INTO aluno_stats
            (user_id, xp, nivel, metas_semanais, aulas_concluidas_semana)
            VALUES (%s, 0, 1, 5, 0)
        """, (user_id,))

    def get_stats(self, user_id):
        res = self.db.query("""
            SELECT *
            FROM aluno_stats
            WHERE user_id = %s
        """, (user_id,))
        return res[0] if res else None

    def get_aulas_concluidas(self, user_id):
        res = self.db.query("""
            SELECT COUNT(DISTINCT aula_id) as total
            FROM progresso
            WHERE user_id = %s
            AND concluido = 1
        """, (user_id,))
        return res[0]["total"] if res else 0

    def get_meta_semanal(self, user_id):
        res = self.db.query("""
            SELECT COUNT(DISTINCT aula_id) as total
            FROM progresso
            WHERE user_id = %s
            AND concluido = 1
            AND data_conclusao >= DATE_SUB(NOW(), INTERVAL 7 DAY)
        """, (user_id,))

        atual = res[0]["total"] if res else 0
        total = 5

        return {
            "atual": atual,
            "total": total,
            "percentual": int((atual / total) * 100) if total else 0
        }

    def get_conquistas(self, user_id):
        res = self.db.query("""
            SELECT c.nome
            FROM user_conquistas uc
            JOIN conquistas c ON c.id = uc.conquista_id
            WHERE uc.user_id = %s
        """, (user_id,))

        return [r["nome"] for r in res] if res else []
    
    def incrementar_xp(self, user_id, xp_ganho):
        self.db.execute("""
        UPDATE aluno_stats
        SET xp = xp + %s
        WHERE user_id = %s
    """, (xp_ganho, user_id))