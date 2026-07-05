from models.certificado_model import CertificadoModel
from models.dashboard_model import DashboardModel
from services.certificado_pdf_service import CertificadoPDFService
from controllers.usuario_controller import UsuarioController

class CertificadoController:

    def __init__(self):
        self.model = CertificadoModel()
        self.dashboard = DashboardModel()
        self.pdf_service = CertificadoPDFService()
        self.usuario = UsuarioController()

    # =========================
    # GERAR CERTIFICADO
    # =========================
    def gerar(self, user_id):

        # 1. garantir stats do usuário
        stats = self.dashboard.get_stats(user_id)

        if not stats:
            return {"erro": "Usuário não encontrado"}

        xp = stats["xp"]
        aulas = self.dashboard.get_aulas_concluidas(user_id)
        usuario = self.usuario.buscar(user_id)

        nome = usuario["nome"] if usuario and "nome" in usuario else f"Aluno {user_id}"

        # 2. regra de liberação
        if aulas < 5:
            return {
                "erro": "Certificado não liberado. Necessário no mínimo 5 aulas concluídas."
            }

        # 3. se já existe, retorna direto
        if self.model.ja_possui(user_id):

            certificado = self.model.buscar(user_id)

            return {
                "status": "ok",
                "message": "Certificado já emitido anteriormente",
                "certificado": certificado,
                "pdf_url": f"/api/certificado/download/{user_id}"
            }

        # 4. GERA PDF PRIMEIRO (arquivo físico)
        caminho_pdf = self.pdf_service.gerar(
            nome=nome,
            xp=xp,
            aulas=aulas,
            user_id=user_id
        )

        # 5. SALVA NO BANCO COM O CAMINHO DO PDF
        self.model.criar(
            user_id=user_id,
            nome=nome,
            xp=xp,
            aulas=aulas,
            arquivo_pdf=caminho_pdf
        )

        # 6. resposta final
        return {
            "status": "ok",
            "message": "Certificado gerado com sucesso",
            "nome": nome,
            "xp": xp,
            "aulas": aulas,
            "pdf_url": f"/api/certificado/download/{user_id}"
        }

    # =========================
    # BUSCAR CERTIFICADO
    # =========================
    def buscar(self, user_id):

        certificado = self.model.buscar(user_id)

        if not certificado:
            return {"erro": "Certificado não encontrado"}

        return {
            "status": "ok",
            "certificado": certificado,
            "pdf_url": f"/api/certificado/download/{user_id}"
        }