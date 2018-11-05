import os
import pickle

class Persistance:
    def __init__(self):
        self._FILE_NAME = "viking.bin"
        self._path = os.path.dirname(__file__) + "/../" + self._FILE_NAME
        self._SERIALIZE_PICKLE_PROTOCOL = 3

    def save(self, login):
        with open(self._path, 'wb') as passwordFile:
            login_dictionary = self.load()
            login_dictionary[login.site] = login
            pickle.dump(login_dictionary, passwordFile, self._SERIALIZE_PICKLE_PROTOCOL)

    def load(self):
        with open(self._path, 'rb') as passwordFile:
            try:
                return pickle.load(passwordFile)
            except EOFError:
                return {}
