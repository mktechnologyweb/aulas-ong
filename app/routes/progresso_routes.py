from flask import Blueprint, jsonify, request
from controllers.progresso_controller import ProgressoController

progresso_bp = Blueprint("progresso_bp", __name__)

prog = ProgressoController()

# =========================
# GET PROGRESSO
# =========================
@progresso_bp.route("/api/progresso/<int:user_id>/<int:aula_id>", methods=["GET"])
def get_progresso(user_id, aula_id):

    res = prog.buscar(user_id, aula_id)

    if not res:
        return jsonify({
            "teoria": False,
            "pratica": False,
            "atividade": False,
            "acertos": 0,
            "total": 0,
            "aprovado": False,
            "concluido": False
        })

    return jsonify(res[0])


# =========================
# POST PROGRESSO
# =========================
@progresso_bp.route("/api/progresso", methods=["POST"])
def salvar_progresso():

    data = request.json
    tipo = data["tipo"]

    if tipo == "teoria":
        prog.salvar_teoria(data["user_id"], data["aula_id"])

    elif tipo == "pratica":
        prog.salvar_pratica(data["user_id"], data["aula_id"])

    elif tipo == "atividade":
        prog.salvar_atividade(
            data["user_id"],
            data["aula_id"],
            data["acertos"],
            data["total"]
        )

    return jsonify({"status": "ok"})