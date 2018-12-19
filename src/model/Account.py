class Account:
    def __init__(self, password_hash, salt):
        self.password_hash = password_hash
        self.salt = salt
