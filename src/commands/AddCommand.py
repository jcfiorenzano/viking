import random
from src.security.Crypt import Crypt
from src.persistance.Persistance import Persistance
from src.model.LoginInfo import LoginInfo


class AddCommand:
    def __init__(self, argument_tuple):
        site = argument_tuple[0]
        username = argument_tuple[1]
        password = argument_tuple[2] if len(argument_tuple) == 3 else None

        self.loginInfo = LoginInfo(site, username, password)

    def execute(self, user_password):
        missing_password = self.loginInfo.password is None
        password = self.loginInfo.password if not missing_password else self._generate_password()

        self.loginInfo.password = Crypt().encrypt(user_password, plain_message=password)

        Persistance().save(self.loginInfo)

        if missing_password:
            return password

    def _generate_password(self):
        password = [None] * 12

        valid_symbols = ["-", "@", "%", ",", "."]

        for i in range(0, 3):
            pos = random.randint(0,12)
            while password[pos] is not None:
                pos = random.randint(0, 12)
            password[pos] = valid_symbols[random.randint(0, len(valid_symbols)-1)]

        for i in range(0, 4):
            pos = random.randint(0, 12)
            while password[pos] is not None:
                pos = random.randint(0, 12)
            password[pos] = chr(random.randint(ord('A'), ord('Z')))

        for i in range(0, 3):
            pos = random.randint(0, 12)
            while password[pos] is not None:
                pos = random.randint(0, 12)
            password[pos] = chr(random.randint(ord('a'), ord('z')))

        for i in range(0, 2):
            pos = random.randint(0, 12)
            while password[pos] is not None:
                pos = random.randint(0, 12)
            password[pos] = str(random.randint(0, 9))

        return "".join(password)