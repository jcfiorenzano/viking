import getpass
import os
import src.config as config
import src.security.SecurityManager as SecurityManager


class Handle:

    def authenticate(self):
        if self.__exist_account():
            password = getpass.getpass()
            return SecurityManager.authenticate(password)
        else:
            self.__create_account()

    def __exist_account(self):
        return os.path.exists(config.ACCOUNT_FILE_PATH)


    def __create_account(self):
        print("Creating new account")
        password = None
        while password is None:
            password = getpass.getpass(prompt="Create Password")
            confirm_password = getpass.getpass(prompt="Confirm Password")

            if password != confirm_password:
                print("Password does not match")
                password = None

        SecurityManager.create_account(password)
