from flask import Blueprint, jsonify, send_file
from controllers.certificado_controller import CertificadoController
import os
cert_bp = Blueprint("cert_bp", __name__)
cert = CertificadoController()

@cert_bp.route("/api/certificado/<int:user_id>", methods=["POST"])
def gerar_certificado(user_id):

    res = cert.gerar(user_id)

    return jsonify(res)


@cert_bp.route("/api/certificado/<int:user_id>", methods=["GET"])
def ver_certificado(user_id):

    res = cert.buscar(user_id)

    if not res:
        return jsonify({"erro": "não encontrado"})

    return jsonify(res)
@cert_bp.route("/api/certificado/download/<int:user_id>", methods=["GET"])
def download_certificado(user_id):

    caminho = f"certificados/certificado_{user_id}.pdf"

    if not os.path.exists(caminho):
        return jsonify({"erro": "PDF não encontrado"}), 404

    return send_file(caminho, as_attachment=True)