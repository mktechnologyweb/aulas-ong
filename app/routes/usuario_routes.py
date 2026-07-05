from flask import Blueprint, jsonify, request

from controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint(
    "usuario_bp",
    __name__
)

controller = UsuarioController()


# =========================
# BUSCAR PERFIL
# =========================
@usuario_bp.route(
    "/api/usuario/<int:user_id>",
    methods=["GET"]
)
def buscar_usuario(user_id):

    usuario = controller.buscar(user_id)

    if not usuario:
        return jsonify({
            "erro": "Usuário não encontrado"
        }), 404

    return jsonify(usuario)


# =========================
# EDITAR PERFIL
# =========================
@usuario_bp.route(
    "/api/usuario/<int:user_id>",
    methods=["PUT"]
)
def atualizar_usuario(user_id):

    data = request.json

    return jsonify(
        controller.atualizar(
            user_id,
            data["nome"],
            data["email"]
        )
    )
@usuario_bp.route(
    "/api/usuario/<int:user_id>/foto",
    methods=["PUT"]
)
def atualizar_foto(user_id):

    data = request.json

    return jsonify(
        controller.atualizar_foto(
            user_id,
            data["foto"]
        )
    )