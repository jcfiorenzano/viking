class LoginInfo:
    def __init__(self, site, username, password):
        self.site = site
        self.username = username
        self.password = password

    def to_string(self):
        return "site: " + self.site + " username: " + self.username + " password: " + self.password
