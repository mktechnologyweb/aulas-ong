from database.db import Database
from services.certificado_pdf_service import CertificadoPDFService

class ProfessorModel:

    def __init__(self):
        self.db = Database()

    # ==========================================
    # CURSOS
    # ==========================================
    def criar_curso(self, nome, descricao, area, professor_id):
        return self.db.execute("""
            INSERT INTO cursos (nome, descricao, area, professor_id)
            VALUES (%s,%s,%s,%s)
        """, (nome, descricao, area, professor_id))

    def listar_cursos(self, professor_id):
        return self.db.query("""
            SELECT *
            FROM cursos
            WHERE professor_id=%s
            ORDER BY id DESC
        """, (professor_id,))

    # ==========================================
    # AULAS
    # ==========================================
    def criar_aula(self, curso_id, titulo, descricao, ordem):
        return self.db.execute("""
            INSERT INTO aulas (curso_id, titulo, descricao, ordem, bloqueada)
            VALUES (%s,%s,%s,%s,0)
        """, (curso_id, titulo, descricao, ordem))

    def listar_aulas(self, curso_id):
        return self.db.query("""
            SELECT *
            FROM aulas
            WHERE curso_id=%s
            ORDER BY ordem
        """, (curso_id,))

    # ==========================================
    # TEORIA
    # ==========================================
    def criar_teoria(self, aula_id, video_url, texto):
        return self.db.execute("""
            INSERT INTO teoria (aula_id, video_url, texto)
            VALUES (%s,%s,%s)
        """, (aula_id, video_url, texto))

    def buscar_teoria(self, aula_id):
        return self.db.query("""
            SELECT *
            FROM teoria
            WHERE aula_id=%s
        """, (aula_id,))

    # ==========================================
    # IMAGENS
    # ==========================================
    def adicionar_imagem(self, teoria_id, imagem_url, ordem):
        return self.db.execute("""
            INSERT INTO teoria_imagens (teoria_id, imagem_url, ordem)
            VALUES (%s,%s,%s)
        """, (teoria_id, imagem_url, ordem))

    def listar_imagens(self, teoria_id):
        return self.db.query("""
            SELECT *
            FROM teoria_imagens
            WHERE teoria_id=%s
            ORDER BY ordem
        """, (teoria_id,))

    # ==========================================
    # ATIVIDADES
    # ==========================================
    def criar_atividade(self, aula_id, pergunta, opcao1, opcao2, opcao3, opcao4, correta):
        return self.db.execute("""
            INSERT INTO atividades
            (aula_id, pergunta, opcao1, opcao2, opcao3, opcao4, correta)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (aula_id, pergunta, opcao1, opcao2, opcao3, opcao4, correta))

    # ==========================================
    # CURSO COMPLETO
    # ==========================================
    def curso_completo(self, curso_id):

        curso = self.db.query("""
            SELECT * FROM cursos WHERE id=%s
        """, (curso_id,))

        if not curso:
            return None

        aulas = self.db.query("""
            SELECT * FROM aulas
            WHERE curso_id=%s
            ORDER BY ordem
        """, (curso_id,))

        for aula in aulas:

            teoria = self.db.query("""
                SELECT * FROM teoria WHERE aula_id=%s
            """, (aula["id"],))

            atividades = self.db.query("""
                SELECT * FROM atividades WHERE aula_id=%s
            """, (aula["id"],))

            aula["teoria"] = teoria
            aula["atividades"] = atividades

        curso[0]["aulas"] = aulas

        return curso[0]

    # ==========================================
    # EDITAR / EXCLUIR CURSO
    # ==========================================
    def editar_curso(self, curso_id, nome, descricao, area):
        return self.db.execute("""
            UPDATE cursos
            SET nome=%s, descricao=%s, area=%s
            WHERE id=%s
        """, (nome, descricao, area, curso_id))

    def excluir_curso(self, curso_id):
        return self.db.execute("""
            DELETE FROM cursos WHERE id=%s
        """, (curso_id,))

    # ==========================================
    # EDITAR / EXCLUIR AULA
    # ==========================================
    def editar_aula(self, aula_id, titulo, descricao, ordem):
        return self.db.execute("""
            UPDATE aulas
            SET titulo=%s, descricao=%s, ordem=%s
            WHERE id=%s
        """, (titulo, descricao, ordem, aula_id))

    def excluir_aula(self, aula_id):
        return self.db.execute("""
            DELETE FROM aulas WHERE id=%s
        """, (aula_id,))

    def listar_alunos(self):
        return self.db.query("""
        SELECT DISTINCT
            u.id,
            u.nome
        FROM users u
        INNER JOIN progresso p
            ON p.user_id = u.id
        ORDER BY u.nome
    """)


    # ==========================================
    # ATIVIDADES DO ALUNO (CORRIGIDO)
    # tabela: progresso
    # ==========================================
    def listar_atividades_por_aluno(self, aluno_id):

        return self.db.query("""
        SELECT
            atividades.id,
            atividades.pergunta,
            atividades.opcao1,
            atividades.opcao2,
            atividades.opcao3,
            atividades.opcao4,

            progresso.acertos,
            progresso.total,
            progresso.nota,
            progresso.aprovado,
            progresso.data_conclusao,
            progresso.aula_id,

            aulas.titulo AS aula_nome,
            cursos.nome AS curso_nome

        FROM progresso

        INNER JOIN aulas
            ON aulas.id = progresso.aula_id

        INNER JOIN cursos
            ON cursos.id = aulas.curso_id

        INNER JOIN atividades
            ON atividades.aula_id = aulas.id

        WHERE progresso.user_id = %s

        ORDER BY progresso.id DESC
    """, (aluno_id,))

    def atividades_do_aluno(self, aluno_id):

     return self.model.listar_atividades_por_aluno(aluno_id)
    
    def dashboard(self, professor_id):

     cursos = self.db.query("""
        SELECT COUNT(*) as total
        FROM cursos
        WHERE professor_id=%s
    """, (professor_id,))[0]["total"]

     aulas = self.db.query("""
        SELECT COUNT(*)
        FROM aulas
        INNER JOIN cursos ON cursos.id = aulas.curso_id
        WHERE cursos.professor_id=%s
    """, (professor_id,))[0]["COUNT(*)"]

     atividades = self.db.query("""
        SELECT COUNT(*)
        FROM atividades
        INNER JOIN aulas ON aulas.id = atividades.aula_id
        INNER JOIN cursos ON cursos.id = aulas.curso_id
        WHERE cursos.professor_id=%s
    """, (professor_id,))[0]["COUNT(*)"]

     alunos = self.db.query("""
        SELECT COUNT(DISTINCT progresso.user_id) as total
        FROM progresso
    """)[0]["total"]

     return {
        "cursos": cursos,
        "aulas": aulas,
        "atividades": atividades,
        "alunos": alunos,
        "aprovacao": 0
    }

       # =========================
    # 👥 ALUNOS
    # =========================
    def listar_alunos(self):
        return self.db.query("""
            SELECT DISTINCT u.id, u.nome
            FROM users u
            INNER JOIN progresso p ON p.user_id = u.id
            ORDER BY u.nome
        """)

    # =========================
    # 📈 EVOLUÇÃO
    # =========================
    def evolucao(self, curso_id):

        query = """
            SELECT
                DATE(p.data_conclusao) as data,
                AVG(p.acertos / p.total * 100) as media
            FROM progresso p
            INNER JOIN aulas a ON a.id = p.aula_id
            WHERE 1=1
        """

        params = []

        if curso_id:
            query += " AND a.curso_id=%s"
            params.append(curso_id)

        query += """
            GROUP BY DATE(p.data_conclusao)
            ORDER BY data ASC
        """

        return self.db.query(query, tuple(params))

    # =========================
    # 🏆 RANKING
    # =========================
    def ranking(self, curso_id):

        query = """
            SELECT
                u.id,
                u.nome AS aluno,
                SUM(p.acertos) AS acertos,
                SUM(p.total) AS total,
                ROUND(AVG(p.acertos / p.total * 100), 2) AS media
            FROM progresso p
            INNER JOIN users u ON u.id = p.user_id
            INNER JOIN aulas a ON a.id = p.aula_id
            WHERE 1=1
        """

        params = []

        if curso_id:
            query += " AND a.curso_id=%s"
            params.append(curso_id)

        query += """
            GROUP BY u.id, u.nome
            ORDER BY media DESC
        """

        return self.db.query(query, tuple(params))
    
    def excluir_curso_completo(self, curso_id):

    # 1. pegar aulas do curso
     aulas = self.db.query("""
        SELECT id FROM aulas WHERE curso_id=%s
    """, (curso_id,))

     for aula in aulas:

        aula_id = aula["id"]

        # atividades
        self.db.execute("""
            DELETE FROM atividades WHERE aula_id=%s
        """, (aula_id,))

        # teoria
        teorias = self.db.query("""
            SELECT id FROM teoria WHERE aula_id=%s
        """, (aula_id,))

        for t in teorias:

            self.db.execute("""
                DELETE FROM teoria_imagens WHERE teoria_id=%s
            """, (t["id"],))

        self.db.execute("""
            DELETE FROM teoria WHERE aula_id=%s
        """, (aula_id,))

        # progresso (se existir ligação)
        self.db.execute("""
            DELETE FROM progresso WHERE aula_id=%s
        """, (aula_id,))

    # aulas
     self.db.execute("""
        DELETE FROM aulas WHERE curso_id=%s
    """, (curso_id,))

    # curso
     self.db.execute("""
        DELETE FROM cursos WHERE id=%s
    """, (curso_id,))
     
    def buscar_curso_edicao(self, curso_id):

     curso = self.db.query("""
        SELECT * FROM cursos WHERE id=%s
    """, (curso_id,))

     if not curso:
        return None

     aulas = self.db.query("""
        SELECT * FROM aulas WHERE curso_id=%s ORDER BY ordem
    """, (curso_id,))

     return {
        "curso": curso[0],
        "aulas": aulas
    }

    def atividades_por_aula(self, aula_id):

     return self.db.query("""
        SELECT *
        FROM atividades
        WHERE aula_id = %s
    """, (aula_id,))

    def get_atividade(self, id):

     result = self.db.query("""
         SELECT
            id,
            aula_id,
            pergunta,
            opcao1,
            opcao2,
            opcao3,
            opcao4,
            correta
        FROM atividades
        WHERE id = %s
    """, (id,))

     return result[0] if result else None
    
    def get_teoria(self, aula_id):

     result = self.db.query("""
        SELECT
            id,
            aula_id,
            video_url,
            texto,
            narracao
        FROM teoria
        WHERE aula_id = %s
    """, (aula_id,))

     return result[0] if result else None
    
    def editar_teoria(self, data):

     self.db.execute("""
        UPDATE teoria
        SET texto = %s,
            video_url = %s,
            narracao = %s
        WHERE aula_id = %s
    """, (
        data["texto"],
        data.get("video_url"),
        data.get("narracao"),
        data["aula_id"]
    ))

     return {"mensagem": "Teoria atualizada"}
    
    def atualizar_atividade(
     self,
     id,
     pergunta,
     opcao1,
     opcao2,
     opcao3,
     opcao4,
     correta
):
 
     sql = """
    UPDATE atividades
    SET
        pergunta=%s,
        opcao1=%s,
        opcao2=%s,
        opcao3=%s,
        opcao4=%s,
        correta=%s
    WHERE id=%s
    """

     return self.db.execute(
         sql,
        (
            pergunta,
            opcao1,
            opcao2,
            opcao3,
            opcao4,
            correta,
            id
        )
    )

    # ==========================================
# DELETE ATIVIDADE
# ==========================================

    
    def excluir_atividade(self, id):

     return self.db.execute("""
        DELETE FROM atividades
        WHERE id=%s
    """, (id,))

    def listar_certificados_professor(self, user, nome=None):

     sql = """

    SELECT

        u.id AS aluno_id,
        u.nome AS aluno,

        c.id AS curso_id,
        c.nome AS curso,

        COUNT(a.id) AS total_aulas,

        NOW() AS emissao


    FROM progresso p


    INNER JOIN users u
    ON u.id = p.user_id


    INNER JOIN aulas a
    ON a.id = p.aula_id


    INNER JOIN cursos c
    ON c.id = a.curso_id


    WHERE c.professor_id = %s

    """


     params=[user["id"]]


     if nome:

        sql += " AND u.nome LIKE %s"

        params.append("%"+nome+"%")


     sql += """

    GROUP BY
    u.id,
    c.id


    ORDER BY aluno

    """


     return self.db.query(sql, tuple(params))
    
    def gerar_certificado(self, aluno_id, curso_id):

     sql = """

    SELECT

        u.id AS user_id,
        u.nome AS aluno,

        c.nome AS curso,

        COUNT(a.id) AS aulas


    FROM users u


    INNER JOIN progresso p
    ON p.user_id = u.id


    INNER JOIN aulas a
    ON a.id = p.aula_id


    INNER JOIN cursos c
    ON c.id = a.curso_id


    WHERE u.id=%s
    AND c.id=%s


    GROUP BY
        u.id,
        c.id

    """


     dados = self.db.query(
        sql,
        (
            aluno_id,
            curso_id
        )
    )


     if not dados:
        raise Exception("Certificado não encontrado")


     user_id = dados[0]["user_id"]

     aluno = dados[0]["aluno"]

     curso = dados[0]["curso"]

     aulas = dados[0]["aulas"]


     pdf = CertificadoPDFService()


     return pdf.gerar(
        aluno,
        curso,
        aulas,
        user_id
    )