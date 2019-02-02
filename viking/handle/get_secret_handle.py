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
            self._show_secret_info(site_url)
        else:
            self._show_all_secrets()


    def _show_secret_info(self, site_url):
        secret = SecretManager.get(site_url)

        if secret is not None:
            self._print_secret_info(secret)
            return

        similar_sites = SecretManager.search(site_url)

        if len(similar_sites) == 0:
            print(print_utils.error_format("We couldn't find a match for the site: {0}".format(site_url)))
            return
        
        if len(similar_sites) == 1:
            secret = SecretManager.get(similar_sites[0])
        else:
            selected_secret = print_utils.print_option_picker(message='Which one do you mean', options=similar_sites)
            secret = SecretManager.get(selected_secret)

        self._print_secret_info(secret)

    def _print_secret_info(self, secret):
        print_utils.print_data_table(["SITE", "USERNAME", "PASSWORD"],[[secret.site, secret.username, secret.password]])
        if secret.security_questions is not None and len(secret.security_questions) != 0:
            print_utils.print_data_table(["QUESTION", "ANSWER"],[[sq[0],sq[1]] for sq in secret.security_questions])
            
    def _show_all_secrets(self):
        secrets = SecretManager.get_all()
        if len(secrets) == 0:
            print(print_utils.error_format("There is no passwords stored."))
        
        headers = ["SITE", "USERNAME", "PASSWORD"]
        secrets_matrix = [[secret.site, secret.username, secret.password] for secret in secrets]
        print_utils.print_data_table(headers, secrets_matrix)