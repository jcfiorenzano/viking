import pickle
import src.config as config

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
