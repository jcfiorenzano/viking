import viking.secret_manager.secret_manager as SecretManager
from viking.handle.handle_base import HandleBase


class ShowCommandHandle(HandleBase):
    def __init__(self, show_arguments):
        self.show_arguments = show_arguments

    def handle(self):
        self.authenticate()
        site_url = self.show_arguments[0] if len(self.show_arguments) > 0 else None

        if site_url is not None:
            self.__show_secret_info(site_url)
        else:
            self.__show_all_secrets()


    def __show_secret_info(self, site_url):
        secret = SecretManager.get(site_url)
        if secret is None:
            print("We couldn't find a match for the site: {0}".format(site_url))
            similar_sites = SecretManager.search(site_url)
            if len(similar_sites) > 0:
                print("Closer results are:")
                for site in similar_sites:
                    print(site)
                print
        else:
            print("Site: {0}".format(secret.site))
            print("Username: {0}".format(secret.username))
            print("Password: {0}".format(secret.password))
            if secret.security_questions is not None and len(secret.security_questions) != 0:
                print("Security Questions:")
                for sq in secret.security_questions:
                    print("Q: {0}".format(sq[0]))
                    print("A: {0}".format(sq[1]))
                    print()

    def __show_all_secrets(self):
        secrets = SecretManager.get_all()
        if len(secrets) == 0:
            print("There is no passwords stored.")
        for secret in secrets:
             print("site: {0} username: {1} password: {2}".format(secret.site, secret.username, secret.password))
