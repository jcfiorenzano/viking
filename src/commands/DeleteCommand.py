from src.persistance.Persistance import Persistance


class DeleteCommand:
    def __init__(self, site_url):
        self.site = site_url

    def execute(self):
        persistance = Persistance()
        persistance.delete(self.site)
