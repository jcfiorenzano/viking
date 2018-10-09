import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Crypt:
    def encrypt(self, password, plain_message):
        fernet = Fernet(self._get_derived_key(password))
        return fernet.encrypt(plain_message)

    def decrypt(self, password, encripted_message):
        fernet = Fernet(self._get_derived_key(password))
        return fernet.decrypt(encripted_message)

    def _get_derived_key(self, password):
        salt = os.urandom(128)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
        return base64.urlsafe_b64encode(kdf.derive(password))
