from flask import Flask
from flask_cors import CORS

from routes.auth_routes import auth_bp
from routes.aula_routes import aula_bp
from routes.progresso_routes import progresso_bp
from routes.dashboard_routes import dashboard_bp
from routes.usuario_routes import usuario_bp
from routes.conquista_routes import conquista_bp
from routes.certificado_routes import cert_bp
from routes.professor_routes import professor_bp
app = Flask(__name__)

CORS(
    app,
    resources={r"/api/*": {"origins": "*"}},
    allow_headers=["Content-Type", "Authorization"],
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"]
)


# =========================
# REGISTRO DAS ROTAS
# =========================
app.register_blueprint(auth_bp)
app.register_blueprint(aula_bp)
app.register_blueprint(progresso_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(conquista_bp)
app.register_blueprint(cert_bp)
app.register_blueprint(professor_bp)
# =========================
# START
# =========================
if __name__ == "__main__":
    app.run(debug=True)