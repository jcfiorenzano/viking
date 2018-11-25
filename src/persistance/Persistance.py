import pickle
import os
import src.config as config
from src.exceptions.Exceptions import SiteNotFound


class Persistance:
    def __init__(self):
        self._SERIALIZE_PICKLE_PROTOCOL = 3

    def save(self, login):
        login_dictionary = self.load()
        login_dictionary[login.site] = login
        with open(config.VIKING_FILE_PATH, 'wb') as passwordFile:
            pickle.dump(login_dictionary, passwordFile, self._SERIALIZE_PICKLE_PROTOCOL)

    def load(self):
        if not os.path.exists(config.VIKING_FILE_PATH):
            return {}

        with open(config.VIKING_FILE_PATH, 'rb') as passwordFile:
            try:
                return pickle.load(passwordFile)
            except EOFError:  # we should get this state is the file exist but it is empty
                return {}

    def delete(self, site):
        logins = self.load()

        if site in logins:
            del (logins[site])
        else:
            raise SiteNotFound

        with open(config.VIKING_FILE_PATH, 'wb') as passwordFile:
            pickle.dump(logins, passwordFile, self._SERIALIZE_PICKLE_PROTOCOL)
