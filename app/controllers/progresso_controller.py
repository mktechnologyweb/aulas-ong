from models.progresso import Progresso
from controllers.dashboard_controller import DashboardController

dash = DashboardController()

class ProgressoController:

    def __init__(self):
        self.model = Progresso()

    def buscar(self, user_id, aula_id):
        return self.model.buscar_progresso(user_id, aula_id)

    def salvar_teoria(self, user_id, aula_id):
        res = self.model.salvar_teoria(user_id, aula_id)

        dash.model.incrementar_meta_semanal(user_id)
        return res

    def salvar_pratica(self, user_id, aula_id):
        res = self.model.salvar_pratica(user_id, aula_id)

        dash.model.incrementar_meta_semanal(user_id)
        return res

    def salvar_atividade(self, user_id, aula_id, acertos, total):

        res = self.model.salvar_atividade(user_id, aula_id, acertos, total)

        porcentagem = (acertos / total) * 100 if total > 0 else 0

        xp = int((acertos / total) * 100) if total > 0 else 0
        dash.add_xp(user_id, "atividade", xp)

        if acertos >= 7:
            dash.model.incrementar_meta_semanal(user_id)
            # aqui você pode manter concluir aula se existir
            # dash.concluir_aula(user_id)

        return res
    
    def dashboard(self, user):

        return self.model.dashboard(user["id"])