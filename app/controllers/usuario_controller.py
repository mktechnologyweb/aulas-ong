from models.usuario import Usuario


class UsuarioController:

    def __init__(self):
        self.model = Usuario()

    # ==========================================
    # CADASTRO
    # ==========================================
    def cadastrar(self, nome, email, senha):
        self.model.cadastrar(nome, email, senha)

    # ==========================================
    # LOGIN
    # ==========================================
    def login(self, email, senha):
        return self.model.login(email, senha)

    # ==========================================
    # BUSCAR POR EMAIL
    # ==========================================
    def buscar_email(self, email):
        return self.model.buscar_email(email)

    # ==========================================
    # GOOGLE
    # ==========================================
    def buscar_google(self, google_id):
        return self.model.buscar_google(google_id)

    def cadastrar_google(self, nome, email, google_id, foto):
        return self.model.cadastrar_google(nome, email, google_id, foto)

    # ==========================================
    # BUSCAR POR ID (IMPORTANTE PRO CERTIFICADO)
    # ==========================================
    def buscar(self, user_id):
        return self.model.buscar_por_id(user_id)

    def atualizar(self, user_id, nome, email):
        self.model.atualizar(user_id, nome, email)
        return {"status": "ok"}

    def atualizar_foto(self, user_id, foto):
        self.model.atualizar_foto(user_id, foto)
        return {"status": "ok"}