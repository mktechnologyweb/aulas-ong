from models.aula import Aula

class AulaController:

    def __init__(self):
        self.model = Aula()

    # =========================
    # UMA AULA
    # =========================
    def buscar(self, aula_id):
        return self.model.get_aula_completa(aula_id)

    # =========================
    # TODAS AS AULAS
    # =========================
    def buscar_todas(self):
        return self.model.get_aulas_completas()