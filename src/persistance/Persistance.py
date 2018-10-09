from src.model import LoginInfo


class Persistance:

    def save(self, login):
        print(login.site+" "+login.username+" "+str(login.password, encoding="utf8"))

    def load(self):
        return LoginInfo()