import base64
import os
import random
import hashlib
import src.config as config
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from src.persistance.AccountRepository import AccountRepository
from src.model.AccountSecret import AccountSecret
from src.exceptions.Exceptions import UserNotAuthenticateException
from src.exceptions.Exceptions import WrongPasswordException


class SecurityManager:
    key = None

    def __init__(self):
        self.__BYTE_ENCODING_FORMAT = "utf8"


    def create_account(self, password):
        salt = os.urandom(config.SALT_SIZE)
        password_hash = self.__get_password_hash(password, salt)
        AccountRepository().save_account(AccountSecret(password_hash, salt))

    def authenticate(self, password):
        if self.__is_password_valid(password):
            key = self.__get_derivaded_key(password)
        raise WrongPasswordException()

    def get_key(self):
        # Todo: need to return the key that we stored
        if self._is_authenticate():
            return b'io_CKnCA0ziUVTaT2KEYuXIre6bQoQTvY6mqeKEtuZc='
        raise UserNotAuthenticateException()

    def encrypt(self, plain_message):
        fernet = Fernet(self.get_key())
        return fernet.encrypt(bytes(plain_message, self.__BYTE_ENCODING_FORMAT))

    def decrypt(self, encrypted_message):
        fernet = Fernet(self.get_key())
        return bytes.decode(fernet.decrypt(encrypted_message), self.__BYTE_ENCODING_FORMAT)

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

    def __get_derivaded_key(self, password):
        account = AccountRepository().load_account()
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                         length=32,
                         salt=account.salt,
                         iterations=100000,
                         backend=default_backend())
        return base64.urlsafe_b64encode(kdf.derive(bytes(password, "utf8")))

    def __is_password_valid(self, password):
        account = AccountRepository().load_account()
        password_hash = self.__get_password_hash(password, account.salt)
        return account.password_hash == password_hash

    def _is_authenticate(self):
        return True

    def __get_password_hash(self, password, salt):
        hash_object = hashlib.sha3_512()
        hash_object.update(password.encode())
        hash_object.update(salt)
        return hash_object.digest()
