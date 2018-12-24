import viking.secret_manager.secret_manager as SecretManager
from viking.handle.handle_base import HandleBase


class DeleteCommandHandle(HandleBase):
    def __init__(self, delete_arguments):
        self.arguments = delete_arguments

    def handle(self):
        self.authenticate()
        site_url = self.arguments[0]
        SecretManager.delete(site_url)