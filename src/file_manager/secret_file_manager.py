import pickle
import jsonpickle
import os
import src.config as config
import src.security.security_manager as SecurityManager
from src.exceptions.exception import SiteNotFound

_SERIALIZE_PICKLE_PROTOCOL = 3


def save(secret):
    secret_dictionary = load()
    secret_dictionary[secret.site] = secret
    __save_dictionary(secret_dictionary)


def load():
    if not os.path.exists(config.VIKING_FILE_PATH):
        return {}

    with open(config.VIKING_FILE_PATH, 'rb') as passwordFile:
        try:
            encripted_content = pickle.load(passwordFile)
            json_dictionary = SecurityManager.decrypt(encripted_content)
            return jsonpickle.decode(json_dictionary)
        except EOFError:  # we should get this state is the file exist but it is empty
            return {}


def delete(site):
    secrets = load()

    if site in secrets:
        del (secrets[site])
    else:
        raise SiteNotFound

    __save_dictionary(secrets)


def __save_dictionary(secret_dictionary):
    encripted_data = SecurityManager.encrypt(jsonpickle.encode(secret_dictionary))
    with open(config.VIKING_FILE_PATH, 'wb') as passwordFile:
        pickle.dump(encripted_data, passwordFile, _SERIALIZE_PICKLE_PROTOCOL)
