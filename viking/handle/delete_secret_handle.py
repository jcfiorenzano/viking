import viking.secret_manager.secret_manager as SecretManager
import viking.util.print_utils as utils
from viking.handle.handle_base import HandleBase


class DeleteCommandHandle(HandleBase):
    def __init__(self, delete_arguments):
        self.arguments = delete_arguments

    def handle(self):
        self.authenticate()
        site_url = self.arguments[0]

        user_answer = ""
        while(user_answer.lower() not in ["n","y"]):
            user_answer = input(utils.warning_format(utils.create_yes_no_question("You are about to remove secrets for the site {0}, do you want to continue?".format(site_url))))
        
        if user_answer.lower() == 'y':
            SecretManager.delete(site_url)