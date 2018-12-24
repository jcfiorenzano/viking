import viking.file_manager.secret_file_manager as SecretFileManager


def add(secret):
    SecretFileManager.save(secret)


def delete(site_url):
    SecretFileManager.delete(site_url)


def get(site_url):
    secrets_dictionary = SecretFileManager.load()
    if len(secrets_dictionary) > 0:
        return secrets_dictionary[site_url]
    return None


def get_all():
    secrets_dictionary = SecretFileManager.load()
    return [secrets_dictionary[key] for key in secrets_dictionary.keys()]
