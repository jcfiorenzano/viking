from src.handle.Handle import Handle


class AddCommandHandle(Handle):
    def __init__(self, add_command):
        self.command = add_command

    def handle(self):
        self.authenticate()
        missing_password = self.command.execute()
        if missing_password is not None:
            print("Your password for this site is: " + missing_password)