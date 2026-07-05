from database.db import Database

class TeoriaModel:

    def __init__(self, db):
        self.db = db

    def criar(self, aula_id, video_url, texto):
        return self.db.query("""
            INSERT INTO teoria (aula_id, video_url, texto)
            VALUES (%s,%s,%s)
        """, (aula_id, video_url, texto))

    def add_imagem(self, teoria_id, imagem_url, ordem):
        return self.db.query("""
            INSERT INTO teoria_imagens (teoria_id, imagem_url, ordem)
            VALUES (%s,%s,%s)
        """, (teoria_id, imagem_url, ordem))

    def get_by_aula(self, aula_id):
        teoria = self.db.query("""
             SELECT * FROM teoria
             WHERE aula_id=%s
             ORDER BY id DESC
             LIMIT 1
        """, (aula_id,))

        if not teoria:
            return None

        imagens = self.db.query("""
            SELECT * FROM teoria_imagens
            WHERE teoria_id=%s
            ORDER BY ordem
        """, (teoria[0]["id"],))

        return {
            "teoria": teoria[0],
            "imagens": imagens
        }
    

    def dashboard(self, professor_id):

     cursos = self.db.query("""
        SELECT COUNT(*) AS total
        FROM cursos
        WHERE professor_id=%s
    """, (professor_id,))[0]["total"]

     aulas = self.db.query("""
        SELECT COUNT(*) AS total
        FROM aulas
        INNER JOIN cursos ON cursos.id = aulas.curso_id
        WHERE cursos.professor_id=%s
    """, (professor_id,))[0]["total"]

     alunos = self.db.query("""
         SELECT COUNT(DISTINCT user_id) AS total
        FROM progresso
    """, ())[0]["total"]

     atividades = self.db.query("""
        SELECT COUNT(*) AS total
        FROM progresso
    """, ())[0]["total"]

     aprovados = self.db.query("""
        SELECT COUNT(*) AS total
        FROM progresso
        WHERE aprovado = 1
    """, ())[0]["total"]

     media = 0
     if atividades > 0:
        media = round((aprovados / atividades) * 100, 2)

     return {
        "cursos": cursos,
        "aulas": aulas,
        "alunos": alunos,
        "atividades": atividades,
        "aprovacao": media
    }

    def editar_teoria(self, data):

     self.db.execute("""
        UPDATE teoria
        SET conteudo = %s
        WHERE aula_id = %s
    """, (data["conteudo"], data["aula_id"]))

     return {"mensagem": "Teoria atualizada"}