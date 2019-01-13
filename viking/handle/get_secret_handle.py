from colorama import Fore
import viking.secret_manager.secret_manager as SecretManager
from viking.handle.handle_base import HandleBase


class ShowCommandHandle(HandleBase):
    def __init__(self, show_argument):
        self.show_argument = show_argument

    def handle(self):
        self.authenticate()
        site_url = self.show_argument if len(self.show_argument) > 0 else None

        if site_url is not None:
            self.__show_secret_info(site_url)
        else:
            self.__show_all_secrets()


    def __show_secret_info(self, site_url):
        secret = SecretManager.get(site_url)
        if secret is None:
            print("{0}We couldn't find a match for the site:{1} {2}".format(Fore.RED, Fore.RESET, site_url))
            similar_sites = SecretManager.search(site_url)
            if len(similar_sites) > 0:
                print("{0}Closer results are:{1}".format(Fore.GREEN, Fore.RESET))
                for site in similar_sites:
                    print(site)
                print
        else:
            print("{0}Site:{1} {2}".format(Fore.GREEN, Fore.RESET, secret.site))
            print("{0}Username:{1} {2}".format(Fore.GREEN, Fore.RESET, secret.username))
            print("{0}Password:{1} {2}".format(Fore.GREEN, Fore.RESET, secret.password))
            if secret.security_questions is not None and len(secret.security_questions) != 0:
                print("{0}Security Questions:{1}".format(Fore.GREEN, Fore.RESET))
                for sq in secret.security_questions:
                    print("{0}Q:{1} {2}".format(Fore.GREEN, Fore.RESET, sq[0]))
                    print("{0}A:{1} {2}".format(Fore.GREEN, Fore.RESET, sq[1]))
                    print()

    def __show_all_secrets(self):
        secrets = SecretManager.get_all()
        if len(secrets) == 0:
            print("{0}There is no passwords stored{1}.".format(Fore.RED, Fore.RESET))
        for secret in secrets:
             print("{0}site:{1} {2} {0}username:{1} {3} {0}password:{1} {4}".format(Fore.GREEN, Fore.RESET, secret.site, secret.username, secret.password))
