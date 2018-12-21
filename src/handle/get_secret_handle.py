import src.secret_manager.secret_manager as SecretManager
from src.handle.handle import Handle


class ShowCommandHandle(Handle):
    def __init__(self, show_arguments):
        self.show_arguments = show_arguments

    def handle(self):
        self.authenticate()
        site_url = self.show_arguments[0] if self.show_arguments is not None else None
        secrets = SecretManager.get(site_url)
        if len(secrets) == 0:
            print("There is no passwords stored for that site.")
        for secret in secrets:
            print("site: {0} username: {1} password: {2}".format(secret.site, secret.username, secret.password))