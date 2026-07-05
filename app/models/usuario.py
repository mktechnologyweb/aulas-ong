from database.db import Database

class Usuario:

    def __init__(self):

        self.db = Database()

    # ==========================================
    # CADASTRO
    # ==========================================
    def cadastrar(self, nome, email, senha):

        return self.db.execute("""
            INSERT INTO users
            (
                nome,
                email,
                senha,
                tipo
            )

            VALUES (%s,%s,%s,'aluno')
        """, (
            nome,
            email,
            senha
        ))

    # ==========================================
    # LOGIN NORMAL
    # ==========================================
    def login(self, email, senha):

        return self.db.query("""
            SELECT *
            FROM users
            WHERE email=%s
            AND senha=%s
        """, (
            email,
            senha
        ))

    # ==========================================
    # BUSCAR EMAIL
    # ==========================================
    def buscar_email(self, email):

        return self.db.query("""
            SELECT *
            FROM users
            WHERE email=%s
        """, (email,))

    # ==========================================
    # GOOGLE
    # ==========================================
    def buscar_google(self, google_id):

        return self.db.query("""
            SELECT *
            FROM users
            WHERE google_id=%s
        """, (google_id,))

    def cadastrar_google(
        self,
        nome,
        email,
        google_id,
        foto
    ):

        return self.db.execute("""
            INSERT INTO users
            (
                nome,
                email,
                google_id,
                foto,
                tipo
            )

            VALUES (%s,%s,%s,%s,'aluno')
        """, (
            nome,
            email,
            google_id,
            foto
        ))
    

  

    def buscar_por_id(self, user_id):

        res = self.db.query("""
         SELECT
            id,
            nome,
            email,
            foto
        FROM users
        WHERE id = %s
    """, (user_id,))

        return res[0] if res else None

        

    def atualizar(self, user_id, nome, email):

        self.db.execute("""
            UPDATE users
            SET
                nome = %s,
                email = %s
            WHERE id = %s
        """, (nome, email, user_id))
    def atualizar_foto(self, user_id, foto):
        
        self.db.execute("""
            UPDATE users
            SET foto=%s
            WHERE id=%s
        """, (foto, user_id))
        