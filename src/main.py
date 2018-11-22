import getpass
import os
import src.config as config
from src.commands.AddCommand import AddCommand
from src.commands.ShowCommand import ShowCommand
from src.commands.DeleteCommand import DeleteCommand
from src.exceptions.Exceptions import UserNotAuthenticateException
from src.exceptions.Exceptions import WrongPasswordException
from src.argumentParser.ArgumentParser import ArgumentParser
from src.security.SecurityManager import SecurityManager

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


def _add(parsed_object):
    executor = AddCommand(parsed_object.add)
    missing_password = executor.execute()
    if missing_password is not None:
        print("Your password for this site is: " + missing_password)


def _show(parsed_object):
    executor = ShowCommand(parsed_object.show)
    logins = executor.execute()
    for login in logins:
        print(login.toString())


def _delete(parsed_object):
    executor = DeleteCommand(parsed_object)
    executor.execute()


def authenticate():
    security = SecurityManager()
    password = getpass.getpass()
    return security.authenticate(password)


def _exist_account():
    return os.path.exists(config.ACCOUNT_FILE_PATH)


def _create_account():
    print("Creating new account")
    password = None
    while password is None:
        password = getpass.getpass(str="Create Password")
        confirm_password = getpass.getpass(str="Confirm Password")

        if password != confirm_password:
            print("Password does not match")
            password = None

    SecurityManager.create_account(password)


if __name__ == "__main__":
    ''' main(sys.argv[1:]) '''
    main("--add site username password".split(" "))
    main("--show site".split(" "))
