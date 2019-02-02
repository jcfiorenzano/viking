import viking.util.print_utils as utils
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
        security_questions = self.__get_security_questions()
        
        if SecretManager.get(site_url) is not None and not self.__is_user_updating() :
            return

        secret = Secret(site_url, username, password, security_questions)
        SecretManager.add(secret)
    
    def __get_security_questions(self):
        user_answer = ""
        while(user_answer.lower() not in ["n","y"]):
            user_answer = input(utils.create_yes_no_question("Do you want to register security questions for this site?"))
        
        security_questions = []
        if user_answer.lower() == "y":
            while(user_answer.lower() == "y"):
                question = input("Enter question: ")
                answer = input("Enter answer: ")
                print()
                
                security_questions.append((question, answer))
                user_answer = ""
                while(user_answer.lower() not in ["n","y"]):
                    user_answer = input(utils.create_yes_no_question("Do you want to continue registering questions?"))
        return security_questions
    
    def __is_user_updating(self):
        user_answer = ""
        while(user_answer.lower() not in ["n","y"]):
            user_answer = input(utils.create_yes_no_question("Your already have stored a secret for this site, do you want to update it?"))

        return user_answer.lower() == "y"

