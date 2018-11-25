import src.security.SecurityManager as SecurityManager
from src.persistance.Persistance import Persistance
from src.model.LoginInfo import LoginInfo


class AddCommand:
    def __init__(self, argument_tuple):
        site = argument_tuple[0]
        username = argument_tuple[1]
        password = argument_tuple[2] if len(argument_tuple) == 3 else None

        self.loginInfo = LoginInfo(site, username, password)

    def execute(self):
        missing_password = self.loginInfo.password is None
        password = self.loginInfo.password if not missing_password else SecurityManager.generate_password()

        self.loginInfo.password = SecurityManager.encrypt(plain_message=password)

        Persistance().save(self.loginInfo)

        if missing_password:
            return password
