from flask import Blueprint, jsonify
from auth import login_required
from controllers.aula_controller import AulaController

aula_bp = Blueprint("aula_bp", __name__)

aula = AulaController()

# =========================
# UMA AULA
# =========================
@aula_bp.route("/api/aula/<int:aula_id>", methods=["GET"])
@login_required
def get_aula(user, aula_id):
    return jsonify(aula.buscar(aula_id))


# =========================
# TODAS AS AULAS
# =========================
@aula_bp.route("/api/aulas", methods=["GET"])
@login_required
def todas_aulas(user):
    return jsonify(aula.buscar_todas())