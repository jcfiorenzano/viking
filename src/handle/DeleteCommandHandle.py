from src.handle.Handle import Handle


class DeleteCommandHandle(Handle):
    def __init__(self, delete_command):
        self.command = delete_command

    def handle(self):
        self.authenticate()
        self.command.execute()