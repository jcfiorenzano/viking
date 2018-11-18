import base64
import os
import random
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from src.exceptions.Exceptions import UserNotAuthenticateException
from src.exceptions.Exceptions import WrongPasswordException


class SecurityManager:
    def __init__(self):
        self._BYTE_ENCODING_FORMAT = "utf8"

    def create_account(self, password):
        # Todo: store password and store key
        self._get_derivaded_key(password="123")
        pass

    def authenticate(self, password):
        # Todo: do something to authenticate the user
        if self._is_password_valid(password):
           pass
        raise WrongPasswordException()

    def get_key(self):
        # Todo: need to return the key that we stored
        if self._is_authenticate():
            return b'io_CKnCA0ziUVTaT2KEYuXIre6bQoQTvY6mqeKEtuZc='
        raise UserNotAuthenticateException()

    def encrypt(self, plain_message):
        fernet = Fernet(self.get_key())
        return fernet.encrypt(bytes(plain_message, self._BYTE_ENCODING_FORMAT))

    def decrypt(self, encrypted_message):
        fernet = Fernet(self.get_key())
        return bytes.decode(fernet.decrypt(encrypted_message), self._BYTE_ENCODING_FORMAT)

    def generate_password(self):
        password = [None] * 12

        valid_symbols = ["-", "@", "%", ",", "."]

        for i in range(0, 3):
            pos = random.randint(0, 12)
            while password[pos] is not None:
                pos = random.randint(0, 12)
            password[pos] = valid_symbols[random.randint(0, len(valid_symbols) - 1)]

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

    def _get_derivaded_key(self, password):
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000,
                         backend=default_backend())
        return base64.urlsafe_b64encode(kdf.derive(bytes(password, "utf8")))

    def _is_password_valid(self, password):
        return True

    def _is_authenticate(self):
        return True