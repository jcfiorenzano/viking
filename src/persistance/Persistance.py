import os
from src.model import LoginInfo
import pickle

class Persistance:
    def __init__(self):
        self.FILE_NAME = "viking.bin"
        self.path = os.path.dirname(__file__)+"/../"+self.FILE_NAME

    def save(self, login):
        PYTHON_BINARY_PROTOCOL = 3

        with open(self.path, 'ab') as passwordFile:
            pickle.dump(login, passwordFile, PYTHON_BINARY_PROTOCOL)

    def load(self):
        return LoginInfo()