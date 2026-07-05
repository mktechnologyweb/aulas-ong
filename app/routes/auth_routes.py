from flask import Blueprint, request, jsonify
import jwt

from auth import gerar_token
from controllers.usuario_controller import UsuarioController

auth_bp = Blueprint("auth_bp", __name__)

userController = UsuarioController()

# =========================
# LOGIN NORMAL
# =========================
@auth_bp.route("/api/login", methods=["POST"])
def login():
    data = request.json

    result = userController.login(
        data["email"],
        data["senha"]
    )

    if not result:
        return jsonify({
            "status": "erro",
            "mensagem": "Login inválido"
        }), 401

    user = result[0]

    token = gerar_token(user)

    return jsonify({
        "status": "ok",
        "token": token,
        "user": user
    })


# =========================
# GOOGLE LOGIN
# =========================
@auth_bp.route("/api/google-login", methods=["POST"])
def google_login():

    data = request.json
    token_google = data.get("token")

    if not token_google:
        return jsonify({
            "status": "erro",
            "mensagem": "Token ausente"
        }), 400

    payload = jwt.decode(
        token_google,
        options={"verify_signature": False}
    )

    email = payload["email"]
    nome = payload["name"]
    google_id = payload["sub"]
    foto = payload.get("picture")

    user = userController.buscar_email(email)

    if not user:
        userController.cadastrar_google(
            nome,
            email,
            google_id,
            foto
        )
        user = userController.buscar_email(email)

    u = user[0]

    token_app = gerar_token(u)

    return jsonify({
        "status": "ok",
        "token": token_app,
        "user": u
    })