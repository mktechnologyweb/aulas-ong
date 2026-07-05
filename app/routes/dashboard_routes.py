from flask import Blueprint, jsonify
from controllers.dashboard_controller import DashboardController
from auth import login_required
dashboard_bp = Blueprint("dashboard_bp", __name__)

dash = DashboardController()

@dashboard_bp.route("/api/dashboard/<int:user_id>", methods=["GET"])

def dashboard(user_id):

    data = dash.get_dashboard(user_id)

    return jsonify(data)


@dashboard_bp.route("/api/xp", methods=["POST"])
def add_xp():

    from flask import request

    data = request.json

    xp = dash.add_xp(
        data["user_id"],
        data.get("tipo", "atividade"),
        data.get("extra", 0)
    )

    return jsonify({
        "status": "ok",
        "xp_ganho": xp
    })
