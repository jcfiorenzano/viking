import getpass
import os
from colorama import Fore
import viking.config as config
import viking.security.security_manager as SecurityManager
import viking.util.print_utils as print_utils

class HandleBase:

    def authenticate(self):
        if self._exist_account():
            password = getpass.getpass()
            return SecurityManager.authenticate(password)
        else:
            self._create_account()

    def _exist_account(self):
        return os.path.exists(config.ACCOUNT_FILE_PATH)


    def _create_account(self):
        print("Creating new account")
        password = None
        while password is None:
            password = getpass.getpass(prompt="Create Password")
            confirm_password = getpass.getpass(prompt="Confirm Password")

            if password != confirm_password:
                print(print_utils.error_format("Password does not match"))
                password = None

        SecurityManager.create_account(password)
