from database.db import Database

class CertificadoModel:

    def __init__(self):
        self.db = Database()

    def ja_possui(self, user_id):
        res = self.db.query("""
            SELECT id
            FROM certificados
            WHERE user_id = %s
        """, (user_id,))
        return len(res) > 0

    def criar(self, user_id, nome, xp, aulas, arquivo_pdf):
     self.db.execute("""
        INSERT INTO certificados
        (user_id, nome, xp, aulas, arquivo_pdf, data_emissao)
        VALUES (%s,%s,%s,%s,%s,NOW())
        """, (user_id, nome, xp, aulas, arquivo_pdf))

    def buscar(self, user_id):
        res = self.db.query("""
            SELECT *
            FROM certificados
            WHERE user_id = %s
        """, (user_id,))
        return res[0] if res else None