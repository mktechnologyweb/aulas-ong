from flask import Blueprint, request, jsonify,send_file

from controllers.professor_controller import ProfessorController
from auth import login_required


professor_bp = Blueprint(
    "professor",
    __name__
)

controller = ProfessorController()


# ==================================================
# CURSOS
# ==================================================

@professor_bp.route(
    "/api/professor/cursos",
    methods=["GET"]
)
@login_required
def meus_cursos(user):

    cursos = controller.meus_cursos(user)

    return jsonify(cursos)



@professor_bp.route(
    "/api/professor/curso",
    methods=["POST"]
)
@login_required
def criar_curso(user):

    data = request.json

    resultado = controller.criar_curso(
        data,
        user
    )

    return jsonify(resultado)



# ==================================================
# AULAS
# ==================================================

@professor_bp.route(
    "/api/professor/aula",
    methods=["POST"]
)
@login_required
def criar_aula(user):

    data = request.json

    resultado = controller.criar_aula(
        data,
        user
    )

    return jsonify(resultado)



# ==================================================
# LISTAR AULAS DO CURSO
# ==================================================

@professor_bp.route(
    "/api/aulas/<int:curso_id>",
    methods=["GET"]
)
@login_required
def listar_aulas(user, curso_id):

    aulas = controller.model.listar_aulas(
        curso_id
    )

    return jsonify(aulas)



# ==================================================
# TEORIA
# ==================================================

@professor_bp.route(
    "/api/professor/teoria",
    methods=["POST"]
)
@login_required
def criar_teoria(user):

    data = request.json


    resultado = controller.criar_teoria(
        data,
        user
    )


    return jsonify(resultado)



# ==================================================
# BUSCAR TEORIA DA AULA
# ==================================================

@professor_bp.route(
    "/api/professor/teoria/<int:aula_id>",
    methods=["GET"]
)
@login_required
def buscar_teoria(user, aula_id):

    resultado = controller.get_teoria(
        aula_id
    )


    return jsonify(resultado)



# ==================================================
# ATIVIDADES
# ==================================================

@professor_bp.route(
    "/api/professor/atividade",
    methods=["POST"]
)
@login_required
def criar_atividade(user):

    data = request.json


    resultado = controller.criar_atividade(
        data,
        user
    )


    return jsonify(resultado)

# ======================================
# EDITAR CURSO
# ======================================

@professor_bp.route(
"/api/professor/curso",
methods=["PUT"]
)
@login_required
def editar_curso(user):

    return jsonify(

        controller.editar_curso(
            request.json,
            user
        )

    )




# ======================================
# DELETE CURSO
# ======================================




    return jsonify(

        controller.excluir_curso(
            id
        )

    )





# ======================================
# EDITAR AULA
# ======================================

@professor_bp.route(
"/api/professor/aula",
methods=["PUT"]
)
@login_required
def editar_aula(user):


    return jsonify(

        controller.editar_aula(
            request.json,
            user
        )

    )





# ======================================
# DELETE AULA
# ======================================

@professor_bp.route(
"/api/professor/aula/<int:id>",
methods=["DELETE"]
)
@login_required
def deletar_aula(user,id):


    return jsonify(

        controller.excluir_aula(
            id
        )

    )

@professor_bp.route(
"/api/professor/curso/<int:id>",
methods=["GET"]
)
@login_required
def curso_completo(user,id):


    return jsonify(

        controller.curso_completo(
            id
        )

    )
@professor_bp.route("/api/professor/alunos", methods=["GET"])
@login_required
def alunos(user):

    return jsonify(
        controller.listar_alunos(user)
    )

@professor_bp.route("/api/professor/atividades-aluno/<int:aluno_id>", methods=["GET"])
@login_required
def atividades_por_aluno(user, aluno_id):

    return jsonify(
        controller.model.listar_atividades_por_aluno(aluno_id)
    )
# ==================================================
# ATIVIDADES DO PROFESSOR
# ==================================================


@professor_bp.route(
    "/api/aluno/atividades",
    methods=["GET"]
)
@login_required
def atividades_aluno(user):

    return jsonify(
        controller.atividades_do_aluno(user)
    )

@professor_bp.route("/api/professor/dashboard", methods=["GET"])
@login_required
def dashboard(user):
    return jsonify(controller.dashboard(user))

@professor_bp.route("/api/professor/alunos", methods=["GET"])
@login_required
def listar_alunos(user):
    return jsonify(controller.listar_alunos(user))

@professor_bp.route(
    "/api/professor/evolucao",
    methods=["GET", "OPTIONS"]
)
@login_required
def evolucao(user):

    curso_id = request.args.get("curso_id")

    return jsonify(
        controller.evolucao(curso_id, user)
    )

@professor_bp.route(
    "/api/professor/ranking",
    methods=["GET", "OPTIONS"]
)
@login_required
def ranking(user):

    curso_id = request.args.get("curso_id")

    return jsonify(
        controller.ranking(curso_id, user)
    )

@professor_bp.route("/api/professor/curso/<int:id>", methods=["DELETE"])
@login_required
def deletar_curso(user, id):

    return jsonify(
        controller.excluir_curso(id, user)
    )

@login_required
def curso_edicao(user, id):

    return jsonify(
        controller.buscar_curso_edicao(id)
    )

@professor_bp.route("/api/professor/atividade-aula/<int:aula_id>", methods=["GET"])
@login_required
def atividades_da_aula(user, aula_id):

    return jsonify(
        controller.atividades_por_aula(aula_id, user)
    )


@professor_bp.route("/api/professor/atividade/<int:id>", methods=["GET"])
@login_required
def get_atividade(user, id):

    return jsonify(
        controller.get_atividade(id, user)
    )


@professor_bp.route("/api/professor/atividade/<int:id>", methods=["PUT"])
@login_required
def atualizar_atividade(user, id):

    data = request.json

    controller.atualizar_atividade(
        id,
        data["pergunta"],
        data["opcao1"],
        data["opcao2"],
        data["opcao3"],
        data["opcao4"],
        data["correta"]
    )

    return jsonify({"ok": True})


@professor_bp.route("/api/professor/atividade/<int:id>", methods=["DELETE"])
@login_required
def deletar_atividade(user, id):

    controller.excluir_atividade(id, user)

    return jsonify({"ok": True})

@professor_bp.route("/api/professor/teoria/<int:aula_id>", methods=["GET"])
@login_required
def get_teoria(user, aula_id):

    return jsonify(
        controller.get_teoria(aula_id)
    )


@professor_bp.route("/api/professor/teoria", methods=["PUT"])
@login_required
def editar_teoria(user):

    data = request.json

    return jsonify(
        controller.editar_teoria(data)
    )

# ==========================================
# CERTIFICADOS PROFESSOR
# ==========================================

@professor_bp.route(
    "/api/professor/certificados",
    methods=["GET"]
)
@professor_bp.route(
"/api/professor/certificados",
methods=["GET"]
)
@login_required
def certificados_professor(user):

    nome = request.args.get("nome")


    return jsonify(
        controller.listar_certificados_professor(
            user,
            nome
        )
    )

@professor_bp.route(
    "/api/professor/certificado/<int:aluno_id>/<int:curso_id>",
    methods=["GET"]
)
@login_required
def baixar_certificado(user, aluno_id, curso_id):

    caminho = controller.gerar_certificado_professor(
        aluno_id,
        curso_id
    )


    return send_file(
        caminho,
        as_attachment=True,
        download_name="certificado.pdf"
    )