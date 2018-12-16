from src.handle.Handle import Handle
from src.commands.DeleteCommand import DeleteCommand


class DeleteCommandHandle(Handle):
    def __init__(self, delete_arguments):
        self.arguments = delete_arguments

    def handle(self):
        self.authenticate()
        site_url = self.arguments[0]
        command = DeleteCommand(site_url)
        command.execute()