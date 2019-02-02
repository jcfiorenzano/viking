from colorama import Fore
import viking.secret_manager.secret_manager as SecretManager
import viking.util.print_utils as print_utils
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
        if secret is not None:
            self.__print_secret_info(secret)
            return
        similar_sites = SecretManager.search(site_url)
        if len(similar_sites) == 0:
            print(print_utils.info_format("We couldn't find a match for the site: {0}".format(site_url)))
        elif len(similar_sites) == 1:
            secret = SecretManager.get(similar_sites[0])
            self.__print_secret_info(secret)
        else:
            print(print_utils.info_format("Which one do you mean?"))
            for site in similar_sites:
                print("- "+site)
            print
        

    def __print_secret_info(self, secret):
        print(print_utils.info_format("Site: ")+secret.site)
        print(print_utils.info_format("Username: ")+secret.username)
        print(print_utils.info_format("Password: ")+secret.password)
        if secret.security_questions is not None and len(secret.security_questions) != 0:
            print(print_utils.info_format("Security Questions:"))
            for sq in secret.security_questions:
                print(print_utils.info_format("Q: ")+sq[0])
                print(print_utils.info_format("A: ")+sq[1])
                print()

    def __show_all_secrets(self):
        secrets = SecretManager.get_all()
        if len(secrets) == 0:
            print(print_utils.error_format("There is no passwords stored."))
        
        headers = ["SITE", "USERNAME", "PASSWORD"]
        secrets_matrix = [[secret.site, secret.username, secret.password] for secret in secrets]
        print_utils.print_data_table(headers, secrets_matrix)