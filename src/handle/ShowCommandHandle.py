from src.handle.Handle import Handle
from src.commands.ShowCommand import ShowCommand


class ShowCommandHandle(Handle):
    def __init__(self, show_arguments):
        self.show_arguments = show_arguments

    def handle(self):
        self.authenticate()
        site_url =self.show_arguments[0] if self.show_arguments is not None else None
        command = ShowCommand(site_url)
        logins = command.execute()
        if len(logins) == 0:
            print("There is no passwords stored for that site.")
        for login in logins:
            print(login.to_string())