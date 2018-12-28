import viking.secret_manager.secret_manager as SecretManager
from viking.handle.handle_base import HandleBase
from viking.model.secret import Secret


class AddCommandHandle(HandleBase):
    def __init__(self, add_command):
        self.add_arguments = add_command

    def handle(self):
        self.authenticate()
        site_url = self.add_arguments[0]
        username = self.add_arguments[1]
        password = input("Insert password: ")

        user_answer = ""
        while(user_answer.lower() not in ["n","y"]):
            user_answer = input("Do you want to register security questions for this site? [Y]es, [N]o ")
        
        security_questions = []
        if user_answer.lower() == "y":
            while(user_answer.lower() == "y"):
                question = input("Enter question: ")
                answer = input("Enter answer: ")
                print()
                
                security_questions.append((question, answer))
                user_answer = ""
                while(user_answer.lower() not in ["n","y"]):
                    user_answer = input("Do you want to continue registering questions? [Y]es, [N]o ")

        secret = Secret(site_url, username, password, security_questions)
        SecretManager.add(secret)
