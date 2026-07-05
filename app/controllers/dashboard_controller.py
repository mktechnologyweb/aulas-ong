from models.dashboard_model import DashboardModel
from controllers.conquista_controller import ConquistaController
conquista_controller = ConquistaController()
class DashboardController:

    def __init__(self):
        self.model = DashboardModel()

    def get_dashboard(self, user_id):

        self.model.ensure_stats(user_id)

        stats = self.model.get_stats(user_id)

        xp = stats["xp"]
        nivel = (xp // 100) + 1

        aulas = self.model.get_aulas_concluidas(user_id)

        meta = self.model.get_meta_semanal(user_id)

        conquistas = conquista_controller.listar(user_id)["conquistas"]

        return {
            "xp": xp,
            "nivel": nivel,
            "aulas": aulas,
            "meta": meta,
            "conquistas": conquistas
        }
    def add_xp(self, user_id, tipo, valor):
      self.model.incrementar_xp(user_id, int(valor))