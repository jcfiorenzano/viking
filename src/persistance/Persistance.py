import pickle
import jsonpickle
import os
import src.config as config
import src.security.SecurityManager as SecurityManager
from src.exceptions.Exceptions import SiteNotFound


class Persistance:
    def __init__(self):
        self._SERIALIZE_PICKLE_PROTOCOL = 3

    def save(self, login):
        login_dictionary = self.load()
        login_dictionary[login.site] = login
        self.__save_dictionary(login_dictionary)

    def load(self):
        if not os.path.exists(config.VIKING_FILE_PATH):
            return {}

        with open(config.VIKING_FILE_PATH, 'rb') as passwordFile:
            try:
                encripted_content = pickle.load(passwordFile)
                json_dictionary = SecurityManager.decrypt(encripted_content)
                return jsonpickle.decode(json_dictionary)
            except EOFError:  # we should get this state is the file exist but it is empty
                return {}

    def delete(self, site):
        logins = self.load()

        if site in logins:
            del (logins[site])
        else:
            raise SiteNotFound

        self.__save_dictionary(logins)

    def __save_dictionary(self, login_dictionary):
        encripted_data = SecurityManager.encrypt(jsonpickle.encode(login_dictionary))
        with open(config.VIKING_FILE_PATH, 'wb') as passwordFile:
            pickle.dump(encripted_data, passwordFile, self._SERIALIZE_PICKLE_PROTOCOL)
