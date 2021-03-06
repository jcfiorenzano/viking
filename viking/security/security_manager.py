import base64
import os
import random
import hashlib
import viking.config as config
import viking.file_manager.account_file_manager as accountRepository
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from viking.model.account import Account
from viking.exceptions.exception import UserNotAuthenticateException
from viking.exceptions.exception import WrongPasswordException

_key = None
_BYTE_ENCODING_FORMAT = "utf8"


def create_account(password):
    salt = os.urandom(config.SALT_SIZE)
    password_hash = _get_password_hash(password, salt)
    accountRepository.save_account(Account(password_hash, salt))
    global _key
    _key = _get_derivaded_key(password)


def authenticate(password):
    if _is_password_valid(password):
        global _key
        _key = _get_derivaded_key(password)
    else:
        raise WrongPasswordException()


def encrypt(plain_message):
    fernet = Fernet(_get_key())
    return fernet.encrypt(bytes(plain_message, _BYTE_ENCODING_FORMAT))


def decrypt(encrypted_message):
    fernet = Fernet(_get_key())
    return bytes.decode(fernet.decrypt(encrypted_message), _BYTE_ENCODING_FORMAT)


def generate_password():
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


def _get_derivaded_key(password):
    account = accountRepository.load_account()
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                     length=32,
                     salt=account.salt,
                     iterations=100000,
                     backend=default_backend())
    return base64.urlsafe_b64encode(kdf.derive(bytes(password, "utf8")))


def _is_authenticated():
    return _key is not None


def _is_password_valid(password):
    account = accountRepository.load_account()
    password_hash = _get_password_hash(password, account.salt)
    return account.password_hash == password_hash


def _get_password_hash(password, salt):
    hash_object = hashlib.sha3_512()
    hash_object.update(password.encode())
    hash_object.update(salt)
    return hash_object.digest()


def _get_key():
    if _is_authenticated():
        return _key
    raise UserNotAuthenticateException()
