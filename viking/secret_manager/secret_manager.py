import viking.file_manager.secret_file_manager as SecretFileManager
import difflib
from urllib.parse import urlparse

def add(secret):
    if secret is None:
        raise ValueError("Incorrect value for secret")

    if secret.site is None or secret.site.strip() == "":
        raise ValueError("The site url can not be empty")

    if secret.username is None or secret.username.strip() == "":
        raise ValueError("The username can not be empty")

    if secret.password is None or secret.password.strip() == "":
        raise ValueError("The password can not be empty")

    SecretFileManager.save(secret)


def delete(site_url):
    SecretFileManager.delete(site_url)

def get(site_url):
    secrets_dictionary = SecretFileManager.load()
    if len(secrets_dictionary) > 0 and site_url in secrets_dictionary:
        return secrets_dictionary[site_url]
    return None

def get_all():
    secrets_dictionary = SecretFileManager.load()
    return [secrets_dictionary[key] for key in secrets_dictionary.keys()]

def search(site):
    secrets_dictionary = SecretFileManager.load()
    return difflib.get_close_matches(site, secrets_dictionary.keys())