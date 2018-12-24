import viking.secret_manager.secret_manager as SecretManager
from viking.handle.handle_base import HandleBase
from viking.model.secret import Secret


class AddCommandHandle(HandleBase):
    def __init__(self, add_command):
        self.add_arguments = add_command

    def handle(self):
        self.authenticate()
        site_url = self.add_arguments[0]
        username = self.add_arguments[1]
        password = input("Insert password: ")

        secret = Secret(site_url, username, password)
        SecretManager.add(secret)
