from models.professor_model import ProfessorModel


class ProfessorController:

    def __init__(self):
        self.model = ProfessorModel()

    # =========================
    # 📚 CURSOS
    # =========================
    def meus_cursos(self, user):

        return self.model.listar_cursos(
            user["id"]
        )

    def criar_curso(self, data, user):

        if not data.get("nome"):

            return {
                "status": "erro",
                "mensagem": "Nome obrigatório"
            }

        curso_id = self.model.criar_curso(
            data["nome"],
            data.get("descricao", ""),
            data.get("area", ""),
            user["id"]
        )

        return {
            "status": "ok",
            "id": curso_id
        }

    # =========================
    # 🎓 AULAS
    # =========================
    def criar_aula(self, data, user):

        curso = self.model.db.query("""
            SELECT id
            FROM cursos
            WHERE id=%s
        """, (data["curso_id"],))

        if not curso:

            return {
                "status": "erro",
                "mensagem": "Curso não encontrado"
            }

        aula_id = self.model.criar_aula(
            data["curso_id"],
            data["titulo"],
            data.get("descricao", ""),
            data.get("ordem", 1)
        )

        return {
            "status": "ok",
            "id": aula_id
        }

    # =========================
    # 📖 TEORIA
    # =========================
    def criar_teoria(self, data, user):

        aula_id = data["aula_id"]

        aula = self.model.db.query("""
            SELECT id
            FROM aulas
            WHERE id=%s
        """, (aula_id,))

        if not aula:

            return {
                "status": "erro",
                "mensagem": "Aula não existe"
            }

        teoria_id = self.model.criar_teoria(
            aula_id,
            data.get("video_url"),
            data.get("texto")
        )

        imagens = data.get("imagens", [])

        for i, img in enumerate(imagens):

            self.model.adicionar_imagem(
                teoria_id,
                img,
                i
            )

        return {
            "status": "ok",
            "teoria_id": teoria_id
        }

    # =========================
    # ❓ ATIVIDADE
    # =========================
    def criar_atividade(self, data, user):

        aula = self.model.db.query("""
            SELECT id
            FROM aulas
            WHERE id=%s
        """, (data["aula_id"],))

        if not aula:

            return {
                "status": "erro",
                "mensagem": "Aula inválida"
            }

        atividade_id = self.model.criar_atividade(
            data["aula_id"],
            data["pergunta"],
            data["opcao1"],
            data["opcao2"],
            data["opcao3"],
            data["opcao4"],
            data["correta"]
        )

        return {
            "status": "ok",
            "id": atividade_id
        }

    # =========================
    # 📖 GET TEORIA
    # =========================
    def get_teoria(self, aula_id):

        teoria = self.model.buscar_teoria(
            aula_id
        )

        if not teoria:
            return None

        imagens = self.model.listar_imagens(
            teoria[0]["id"]
        )

        return {
            "teoria": teoria[0],
            "imagens": imagens
        }

    # =========================
    # EDITAR CURSO
    # =========================
    def editar_curso(self, data, user):

        self.model.editar_curso(
            data["id"],
            data["nome"],
            data.get("descricao", ""),
            data.get("area", "")
        )

        return {
            "status": "ok",
            "mensagem": "Curso atualizado"
        }

    # =========================
    # EXCLUIR CURSO
    # =========================
    def excluir_curso(self, curso_id):

        self.model.excluir_curso(curso_id)

        return {
            "status": "ok"
        }

    # =========================
    # EDITAR AULA
    # =========================
    def editar_aula(self, data, user):

        self.model.editar_aula(
            data["id"],
            data["titulo"],
            data.get("descricao", ""),
            data.get("ordem", 1)
        )

        return {
            "status": "ok"
        }

    # =========================
    # EXCLUIR AULA
    # =========================
    def excluir_aula(self, aula_id):

        self.model.excluir_aula(aula_id)

        return {
            "status": "ok"
        }

    # =========================
    # CURSO COMPLETO
    # =========================
    def curso_completo(self, curso_id):

        return self.model.curso_completo(curso_id)

    def listar_alunos(self, user):

        return self.model.listar_alunos()
    # =========================
    # LISTAR ATIVIDADES
    # =========================
   # =========================
    # LISTAR ATIVIDADES DO ALUNO
    # =========================
    def atividades_do_aluno(self, user):

        return self.model.listar_atividades_por_aluno(
            user["id"]
        )
    
    def dashboard(self, user):
     return self.model.dashboard(user["id"])
    
    def listar_alunos(self, user):
        return self.model.listar_alunos()

    # =========================
    # 📈 EVOLUÇÃO
    # =========================
    def evolucao(self, curso_id, user):
        return self.model.evolucao(curso_id)

    # =========================
    # 🏆 RANKING
    # =========================
    def ranking(self, curso_id, user):
        return self.model.ranking(curso_id)
    
    def excluir_curso(self, curso_id, user):

     self.model.excluir_curso_completo(curso_id)

     return {
        "status": "ok",
        "mensagem": "Curso e dependências removidos"
    }
    def atividades_por_aula(self, aula_id, user):

     return self.model.atividades_por_aula(aula_id)
    
    def get_atividade(self, id, user):

     return self.model.get_atividade(id)
    
    def get_teoria(self, aula_id):
     return self.model.get_teoria(aula_id)
    
    def editar_teoria(self, data):
     return self.model.editar_teoria(data)
    
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

     return self.model.atualizar_atividade(
        id,
        pergunta,
        opcao1,
        opcao2,
        opcao3,
        opcao4,
        correta
    )
# ==========================================
# EXCLUIR ATIVIDADE
# ==========================================

    def excluir_atividade(self, id, user):

     return self.model.excluir_atividade(id)
    
    def listar_certificados_professor(self,user,nome=None):

     return self.model.listar_certificados_professor(
        user,
        nome
    )
    def gerar_certificado_professor(self, aluno_id, curso_id):

     return self.model.gerar_certificado(
        aluno_id,
        curso_id
    )