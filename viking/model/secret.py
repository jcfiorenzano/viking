class Secret:
    def __init__(self, site, username, password, security_questions = []):
        self.site = site
        self.username = username
        self.password = password
        self.security_questions = security_questions
