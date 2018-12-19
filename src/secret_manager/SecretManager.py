import src.file_manager.SecretFileManager as SecretFileManager


def add(secret):
    SecretFileManager.save(secret)


def delete(site_url):
    SecretFileManager.delete(site_url)


def get(site_url):
    login_info_dictionary = SecretFileManager.load()
    if len(login_info_dictionary) == 0:
        return []

    result = []
    if not site_url:
        for login_key in login_info_dictionary.keys():
            result.append(login_info_dictionary[login_key])
    else:
        login = login_info_dictionary[site_url]
        result.append(login)

    return result
