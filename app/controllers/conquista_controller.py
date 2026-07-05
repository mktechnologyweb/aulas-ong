from models.conquista_model import ConquistaModel

class ConquistaController:

    def __init__(self):
        self.model = ConquistaModel()

    def verificar_conquistas(self, user_id):

        aulas = self.model.total_aulas(user_id)
        xp = self.model.total_xp(user_id)

        # Primeira aula
        if aulas >= 1:
            self.model.adicionar_conquista(user_id, 1)

        # 5 aulas
        if aulas >= 5:
            self.model.adicionar_conquista(user_id, 2)

        # 10 aulas
        if aulas >= 10:
            self.model.adicionar_conquista(user_id, 3)

        # 100 xp
        if xp >= 100:
            self.model.adicionar_conquista(user_id, 4)

        # 500 xp
        if xp >= 500:
            self.model.adicionar_conquista(user_id, 5)

    def listar(self, user_id):

        self.verificar_conquistas(user_id)

        todas = self.model.listar_todas()

        usuario = self.model.listar_usuario(user_id)

        ids_usuario = [
            c["conquista_id"]
            for c in usuario
        ]

        desbloqueadas = 0

        for conquista in todas:

            conquista["desbloqueada"] = (
                conquista["id"] in ids_usuario
            )

            if conquista["desbloqueada"]:
                desbloqueadas += 1

        percentual = 0

        if len(todas) > 0:
            percentual = int(
                (desbloqueadas / len(todas)) * 100
            )

        return {
            "desbloqueadas": desbloqueadas,
            "percentual": percentual,
            "conquistas": todas
        }