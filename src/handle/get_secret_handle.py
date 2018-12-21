import src.secret_manager.secret_manager as SecretManager
from src.handle.handle import Handle


class ShowCommandHandle(Handle):
    def __init__(self, show_arguments):
        self.show_arguments = show_arguments

    def handle(self):
        self.authenticate()
        site_url = self.show_arguments[0]

        if site_url is not None:
            self.__show_secret_info(site_url)
        else:
            self.show_all_secrets()


    def __show_secret_info(self, site_url):
        secret = SecretManager.get(site_url)
        if secret is None:
            print("There is no passwords stored for that site.")
        else:
            self.__print_secret(secret)

    def __show_all_secrets(self):
        secrets = SecretManager.get_all()
        if len(secrets) == 0:
            print("There is no passwords stored for that site.")
        for secret in secrets:
            self.__print_secret(secret)

    def __print_secret(self, secret):
        print("site: {0} username: {1} password: {2}".format(secret.site, secret.username, secret.password))