import src.secret_manager.SecretManager as SecretManager
from src.handle.Handle import Handle
from src.model.Secret import Secret


class AddCommandHandle(Handle):
    def __init__(self, add_command):
        self.add_arguments = add_command

    def handle(self):
        self.authenticate()
        site_url = self.add_arguments[0]
        username = self.add_arguments[1]
        password = input("Insert password: ")

        secret = Secret(site_url, username, password)
        SecretManager.add(secret)
