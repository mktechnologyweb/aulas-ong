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
@auth_bp.route("/api/login-google", methods=["POST", "OPTIONS"])
def google_login():
    if request.method == "OPTIONS":
        return "", 200

    data = request.json
    token_google = data.get("token")

    if not token_google:
        return jsonify({
            "status": "erro",
            "mensagem": "Token ausente"
        }), 400

    try:
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

        # Garante a extração correta do primeiro registro retornado do banco
        u = user[0] if isinstance(user, (list, tuple)) else user

        # CASO SEU BANCO RETORNE TUPLA (ex: (1, 'Nome', 'email@', 'aluno')), CONVERTA PARA DICIONÁRIO MANUALMENTE:
        # Se 'u' já for um dicionário e tiver chaves como u['id'], u['nome'], u['tipo'], o bloco abaixo será ignorado.
        if isinstance(u, (tuple, list)):
            u = {
                "id": u[0],      # Altere os índices se a ordem das colunas do seu SELECT for diferente
                "nome": u[1],
                "email": u[2],
                "tipo": "aluno"   # Força o tipo como aluno para bater com as travas do front
            }
        elif isinstance(u, dict) and "tipo" not in u:
            u["tipo"] = "aluno" # Garante que a chave exista no dicionário

        token_app = gerar_token(u)

        return jsonify({
            "status": "ok",
            "token": token_app,
            "user": u
        }), 200

    except Exception as e:
        return jsonify({
            "status": "erro",
            "mensagem": f"Erro interno ao processar login: {str(e)}"
        }), 500