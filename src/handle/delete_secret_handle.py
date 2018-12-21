import src.secret_manager.secret_manager as SecretManager
from src.handle.handle import Handle


class DeleteCommandHandle(Handle):
    def __init__(self, delete_arguments):
        self.arguments = delete_arguments

    def handle(self):
        self.authenticate()
        site_url = self.arguments[0]
        SecretManager.delete(site_url)