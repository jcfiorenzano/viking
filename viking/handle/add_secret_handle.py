import viking.util.print_utils as print_utils
import viking.secret_manager.secret_manager as SecretManager
from viking.handle.handle_base import HandleBase
from viking.model.secret import Secret


class AddCommandHandle(HandleBase):
    def __init__(self, add_command):
        self.add_arguments = add_command

    def handle(self):
        self.authenticate()
        site_url = self.add_arguments[0]
        
        if SecretManager.get(site_url) is not None and not self._is_user_updating() :
            return

        username = self.add_arguments[1]
        password = input("Insert password: ")
        security_questions = self._get_security_questions()
        
        secret = Secret(site_url, username, password, security_questions)
        SecretManager.add(secret)
    
    def _get_security_questions(self):
        user_confirm = print_utils.ask_yes_no_question("Do you want to register security questions for this site")
        
        security_questions = []
        if user_confirm:
            while(user_confirm):
                question = input(print_utils.info_format("Question: "))
                answer = input(print_utils.info_format("Answer: "))
                print()
                
                security_questions.append((question, answer))
                user_confirm = print_utils.ask_yes_no_question("Do you want to continue registering questions")
        return security_questions
    
    def _is_user_updating(self):
        user_confirm = print_utils.ask_yes_no_question("Your already have stored a secret for this site, do you want to update it?")
        return user_confirm

