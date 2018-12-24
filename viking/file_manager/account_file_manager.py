import viking.config as config
from viking.model.account import Account


def load_account():
    with open(config.ACCOUNT_FILE_PATH, "rb") as account_file:
        stored_salt = account_file.read(config.SALT_SIZE)
        stored_password_hash = account_file.read()
        return Account(stored_password_hash, stored_salt)


def save_account(account_secret):
    with open(config.ACCOUNT_FILE_PATH, "wb") as account_file:
        account_file.write(account_secret.salt)
        account_file.write(account_secret.password_hash)
