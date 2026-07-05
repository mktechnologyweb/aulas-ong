from flask import Blueprint, jsonify

from controllers.conquista_controller import ConquistaController

conquista_bp = Blueprint(
    "conquista_bp",
    __name__
)

controller = ConquistaController()

@conquista_bp.route(
    "/api/conquistas/<int:user_id>",
    methods=["GET"]
)
def listar_conquistas(user_id):

    return jsonify(
        controller.listar(user_id)
    )