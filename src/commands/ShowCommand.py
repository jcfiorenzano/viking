from src.persistance.Persistance import Persistance
from src.security.SecurityManager import SecurityManager


class ShowCommand:
    def __init__(self, argument):
        self.site_url = argument[0] if argument is not None else None

    def execute(self):
        login_info_dictionary = Persistance().load()

        if not self.site_url:
            for login_key in login_info_dictionary.keys():
                print(login_key)
        else:
            login_info = login_info_dictionary[self.site_url]
            login_info.password = SecurityManager().decrypt(login_info.password)
            print(login_info.toString())
