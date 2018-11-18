import pickle
import src.config as config
from src.exceptions.Exceptions import SiteNotFound

class Persistance:
    def __init__(self):
        self._SERIALIZE_PICKLE_PROTOCOL = 3

    def save(self, login):
        with open(config.VIKING_FILE_PATH, 'wb') as passwordFile:
            login_dictionary = self.load()
            login_dictionary[login.site] = login
            pickle.dump(login_dictionary, passwordFile, self._SERIALIZE_PICKLE_PROTOCOL)

    def load(self):
        with open(config.VIKING_FILE_PATH, 'rb') as passwordFile:
            try:
                return pickle.load(passwordFile)
            except EOFError:
                return {}

    def delete(self, site):
        logins = self.load()

        if site in logins:
            del(logins[site])
        else:
            raise SiteNotFound

        with open(config.VIKING_FILE_PATH, 'wb') as passwordFile:
            pickle.dump(logins, passwordFile, self._SERIALIZE_PICKLE_PROTOCOL)