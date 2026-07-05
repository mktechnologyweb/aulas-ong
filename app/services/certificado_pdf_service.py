from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime
import os


class CertificadoPDFService:

    def gerar(self, nome, xp, aulas, user_id):

        pasta = "certificados"
        os.makedirs(pasta, exist_ok=True)

        caminho = f"{pasta}/certificado_{user_id}.pdf"

        c = canvas.Canvas(caminho, pagesize=A4)
        largura, altura = A4  # retrato padrão

        # =========================
        # FUNDO (MOLDURA ELEGANTE)
        # =========================
        c.setStrokeColor(colors.HexColor("#1f3a93"))
        c.setLineWidth(3)
        c.rect(40, 40, largura - 80, altura - 80)

        c.setStrokeColor(colors.HexColor("#dcdcdc"))
        c.setLineWidth(1)
        c.rect(55, 55, largura - 110, altura - 110)

        # =========================
        # LOGO
        # =========================
        logo_path = "static/logo.jpeg"

        if os.path.exists(logo_path):
            c.drawImage(
                logo_path,
                largura / 2 - 35,
                altura - 120,
                width=70,
                height=70,
                mask='auto'
            )

        # =========================
        # ONG / INSTITUIÇÃO
        # =========================
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(colors.HexColor("#1f3a93"))
        c.drawCentredString(
            largura / 2,
            altura - 140,
            "ONG - Plataforma de Ensino"
        )

        # linha decorativa
        c.setStrokeColor(colors.HexColor("#1f3a93"))
        c.setLineWidth(1)
        c.line(180, altura - 155, 430, altura - 155)

        # =========================
        # TÍTULO
        # =========================
        c.setFont("Helvetica-Bold", 30)
        c.setFillColor(colors.black)
        c.drawCentredString(largura / 2, altura - 230, "CERTIFICADO")

        c.setFont("Helvetica", 16)
        c.drawCentredString(largura / 2, altura - 260, "DE CONCLUSÃO")

        # =========================
        # NOME DO ALUNO (DESTAQUE)
        # =========================
        c.setFont("Helvetica-Bold", 22)
        c.setFillColor(colors.HexColor("#1f3a93"))
        c.drawCentredString(largura / 2, altura - 320, nome)

        # =========================
        # TEXTO
        # =========================
        c.setFont("Helvetica", 12)
        c.setFillColor(colors.black)

        texto = f"""
        Concluiu com êxito todas as atividades do curso,
        demonstrando dedicação e desempenho satisfatório.

        Aulas concluídas: {aulas}
        Pontuação XP: {xp}
        """

        y = altura - 380

        for linha in texto.split("\n"):
            linha = linha.strip()
            if linha:
                c.drawCentredString(largura / 2, y, linha)
                y -= 18

        # =========================
        # DATA
        # =========================
        data = datetime.now().strftime("%d/%m/%Y")

        c.setFont("Helvetica-Oblique", 11)
        c.setFillColor(colors.grey)
        c.drawCentredString(largura / 2, 140, f"Emitido em {data}")

        # =========================
        # ASSINATURAS
        # =========================
        c.setStrokeColor(colors.black)

        # linha esquerda
        c.line(120, 100, 260, 100)
        c.setFont("Helvetica", 10)
        c.drawCentredString(190, 80, "Coordenador")

        # linha direita
        c.line(340, 100, 480, 100)
        c.drawCentredString(410, 80, "Direção")

        # =========================
        # FINALIZA
        # =========================
        c.save()

        return caminho