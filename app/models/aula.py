from database.db import Database

class Aula:

    def __init__(self):
        self.db = Database()

    # =========================
    # UMA AULA
    # =========================
    def get_aula_completa(self, aula_id):

        aula = self.db.query("""
            SELECT *
            FROM aulas
            WHERE id=%s
        """, (aula_id,))

        # =========================
        # TEORIA
        # PEGA A MAIS RECENTE
        # =========================
        teoria = self.db.query("""
            SELECT *
            FROM teoria
            WHERE aula_id=%s
            ORDER BY id DESC
            LIMIT 1
        """, (aula_id,))

        teoria_data = teoria[0] if teoria else {}

        # =========================
        # IMAGENS DA TEORIA
        # =========================
        imagens = []

        if teoria_data:

            imagens = self.db.query("""
                SELECT *
                FROM teoria_imagens
                WHERE teoria_id=%s
                ORDER BY ordem
            """, (teoria_data["id"],))

        teoria_data["imagens"] = imagens

        # =========================
        # PRATICA
        # =========================
        pratica = self.db.query("""
            SELECT *
            FROM pratica
            WHERE aula_id=%s
            ORDER BY ordem
        """, (aula_id,))

        # =========================
        # ATIVIDADES
        # =========================
        atividades = self.db.query("""
            SELECT *
            FROM atividades
            WHERE aula_id=%s
        """, (aula_id,))

        return {
            "aula": aula[0] if aula else {},
            "teoria": teoria_data,
            "pratica": pratica,
            "atividades": atividades
        }

    # =========================
    # TODAS AS AULAS
    # =========================
    def get_aulas_completas(self):

        aulas = self.db.query("""
            SELECT *
            FROM aulas
            ORDER BY ordem ASC, id ASC
        """)

        resultado = []

        for a in aulas:

            aula_id = a["id"]

            # =========================
            # TEORIA
            # =========================
            teoria = self.db.query("""
                SELECT *
                FROM teoria
                WHERE aula_id=%s
                ORDER BY id DESC
                LIMIT 1
            """, (aula_id,))

            teoria_data = teoria[0] if teoria else {}

            imagens = []

            if teoria_data:

                imagens = self.db.query("""
                    SELECT *
                    FROM teoria_imagens
                    WHERE teoria_id=%s
                    ORDER BY ordem
                """, (teoria_data["id"],))

            teoria_data["imagens"] = imagens

            # =========================
            # PRATICA
            # =========================
            pratica = self.db.query("""
                SELECT *
                FROM pratica
                WHERE aula_id=%s
                ORDER BY ordem
            """, (aula_id,))

            # =========================
            # ATIVIDADES
            # =========================
            atividades = self.db.query("""
                SELECT *
                FROM atividades
                WHERE aula_id=%s
            """, (aula_id,))

            resultado.append({
                "aula": a,
                "teoria": teoria_data,
                "pratica": pratica,
                "atividades": atividades
            })

        return resultado