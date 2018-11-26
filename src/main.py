import sys
import getpass
import os
import src.config as config
from src.commands.AddCommand import AddCommand
from src.commands.ShowCommand import ShowCommand
from src.commands.DeleteCommand import DeleteCommand
from src.exceptions.Exceptions import UserNotAuthenticateException
from src.exceptions.Exceptions import WrongPasswordException
from src.argumentParser.ArgumentParser import ArgumentParser
import src.security.SecurityManager as SecurityManager

'''
COMMANDS:
    Add
        This creates a new relation between a password, username and site
        the site argument does not require to be a URL, it could be just a name
        the command is:
        
        -a site username [password]
        
        if the password is left blank then the application is going to generate one
        
    Show
        Given a site it shows the relation username password for that site
        if note site is passed it shows all sites registered, the user has
        to provide the key to execute this command, the command definition is:
        -s [site]
    Delete
        Remove an entry of the database
        -d site
'''


def main(argv):
    if _exist_account():
        authenticate()
    else:
        _create_account()
    _process_input(argv)


def _process_input(argv):
    try:
        parser = ArgumentParser()
        parsed_object = parser.parse(argv)

        if parsed_object.add:
            _add(parsed_object.add)
        elif parsed_object.show:
            _show(parsed_object.show)
        elif parsed_object.delete:
            _delete(parsed_object.delete)

    except WrongPasswordException:
        print("Password incorrect")
    except UserNotAuthenticateException:
        print("Fail to authenticate the user")
    except Exception:
        print("An unexpected exception was raised")


def _add(args):
    executor = AddCommand(args)
    missing_password = executor.execute()
    if missing_password is not None:
        print("Your password for this site is: " + missing_password)


def _show(args):
    executor = ShowCommand(args)
    logins = executor.execute()
    if len(logins) == 0:
        print("There is no passwords stored for that site.")
    for login in logins:
        print(login.to_string())


def _delete(args):
    executor = DeleteCommand(args)
    executor.execute()


def authenticate():
    password = getpass.getpass()
    return SecurityManager.authenticate(password)


def _exist_account():
    return os.path.exists(config.ACCOUNT_FILE_PATH)


def _create_account():
    print("Creating new account")
    password = None
    while password is None:
        password = getpass.getpass(prompt="Create Password")
        confirm_password = getpass.getpass(prompt="Confirm Password")

        if password != confirm_password:
            print("Password does not match")
            password = None

    SecurityManager.create_account(password)


if __name__ == "__main__":
     main(sys.argv[1:])
    # main("-a asd asd asd".split())
    # main("-s asd".split())
    # main("-d asd".split())
    # main("-s asd".split())
    # main("-a bcb bcb bcb".split())

