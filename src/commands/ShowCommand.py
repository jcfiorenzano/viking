from src.persistance.Persistance import Persistance
import src.security.SecurityManager as SecurityManager


class ShowCommand:
    def __init__(self, site_url):
        self.site_url = site_url

    def execute(self):
        login_info_dictionary = Persistance().load()
        if len(login_info_dictionary) == 0:
            return []

        result = []
        if not self.site_url:
            for login_key in login_info_dictionary.keys():
                result.append(login_info_dictionary[login_key])
        else:
            login = login_info_dictionary[self.site_url]
            result.append(login)

        return result
