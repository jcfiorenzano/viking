from src.persistance.Persistance import Persistance
import src.security.SecurityManager as SecurityManager


class ShowCommand:
    def __init__(self, argument):
        self.site_url = argument[0] if argument is not None else None

    def execute(self):
        login_info_dictionary = Persistance().load()
        if len(login_info_dictionary) == 0:
            return []

        result = []
        if not self.site_url:
            for login_key in login_info_dictionary.keys():
                login = login_info_dictionary[login_key]
                login.password = SecurityManager.decrypt(login.password)
                result.append(login)
        else:
            login = login_info_dictionary[self.site_url]
            login.password = SecurityManager.decrypt(login.password)
            result.append(login)

        return result
