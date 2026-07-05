import jwt
import datetime
from flask import request, jsonify
from functools import wraps

SECRET = "MINHA_CHAVE_SUPER_SECRETA_2026_SISTEMA_ONG_EDUCAFUTURO_123456"

# =========================
# GERAR TOKEN
# =========================
def gerar_token(user):

    payload = {
        "id": user["id"],
        "nome": user["nome"],
        "email": user["email"],
        "tipo": user["tipo"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }

    return jwt.encode(payload, SECRET, algorithm="HS256")

# =========================
# VALIDAR TOKEN
# =========================
def verificar_token(token):

    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])

    except jwt.ExpiredSignatureError:
        print("TOKEN EXPIRADO")
        return None

    except jwt.InvalidTokenError as e:
        print("TOKEN INVALIDO:", e)
        return None

# =========================
# LOGIN REQUIRED
# =========================
def login_required(f):

    @wraps(f)
    def wrapper(*args, **kwargs):

        # ✅ LIBERA PRE-FLIGHT CORS
        if request.method == "OPTIONS":
            return "", 200

        auth = request.headers.get("Authorization")

        if not auth:
            return jsonify({"mensagem": "Sem token"}), 401

        token = auth.replace("Bearer ", "").strip()

        user = verificar_token(token)

        if not user:
            return jsonify({"mensagem": "Token inválido"}), 401

        return f(user, *args, **kwargs)

    return wrapper
# =========================
# STAFF REQUIRED
# =========================
def staff_required(f):

    @wraps(f)
    def wrapper(*args, **kwargs):

        if request.method == "OPTIONS":
            return "", 200

        auth = request.headers.get("Authorization")

        if not auth:
            return jsonify({"mensagem": "Sem token"}), 401

        token = auth.replace("Bearer ", "").strip()

        user = verificar_token(token)

        if not user:
            return jsonify({"mensagem": "Token inválido"}), 401

        if user["tipo"] not in ["professor", "admin"]:
            return jsonify({"mensagem": "Acesso negado"}), 403

        return f(user, *args, **kwargs)

    return wrapper