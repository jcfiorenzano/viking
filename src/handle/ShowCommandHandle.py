from src.handle.Handle import Handle


class ShowCommandHandle(Handle):
    def __init__(self, show_command):
        self.command = show_command

    def handle(self):
        self.authenticate()
        logins = self.command.execute()
        if len(logins) == 0:
            print("There is no passwords stored for that site.")
        for login in logins:
            print(login.to_string())