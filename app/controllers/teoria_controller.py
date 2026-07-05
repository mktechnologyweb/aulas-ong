from models.teoria_model import TeoriaModel
from database.db import Database

class TeoriaController:

    def __init__(self):
        self.model = TeoriaModel(Database())

    def criar_teoria(self, data, user):

        aula_id = data["aula_id"]

        # 🔥 validação obrigatória (resolve foreign key error)
        existe = self.model.db.query(
            "SELECT id FROM aulas WHERE id=%s",
            (aula_id,)
        )

        if not existe:
            return {"erro": "Aula não existe"}

        teoria_id = self.model.criar(
            aula_id,
            data.get("video_url"),
            data.get("texto")
        )

        imagens = data.get("imagens", [])

        for i, img in enumerate(imagens):
            self.model.add_imagem(teoria_id, img, i)

        return {"status": "ok"}

    def get_teoria(self, aula_id):
        return self.model.get_by_aula(aula_id)