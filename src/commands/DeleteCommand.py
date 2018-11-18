from src.persistance.Persistance import Persistance


class DeleteCommand:
    def __init__(self, parsed_argument):
        self.site = parsed_argument[0]

    def execute(self):
        persistance = Persistance()
        persistance.delete(self.site)
