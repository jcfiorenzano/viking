import src.security.SecurityManager as SecurityManager
from src.persistance.Persistance import Persistance
from src.model.LoginInfo import LoginInfo


class AddCommand:
    def __init__(self, site, username, password):
        site = site
        username = username
        password = password

        self.loginInfo = LoginInfo(site, username, password)

    def execute(self):
        Persistance().save(self.loginInfo)
