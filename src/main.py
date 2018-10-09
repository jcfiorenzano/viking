import getpass
from src.commands.AddCommand import AddCommand
from src.exceptions.Exceptions import WrongPasswordException
from src.argumentParser.ArgumentParser import ArgumentParser

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
        -d username site
'''

def main(argv):
    try:
        parser = ArgumentParser()
        parsed_object = parser.parse(argv)
        password = ask_password()

        if parsed_object.add:
            executor = AddCommand(parsed_object.add)
            executor.execute(password)
        elif parsed_object.show:
            print()
        elif parsed_object.delete:
            print()
    except WrongPasswordException:
        print("Password incorrect")
    # except Exception:
    #     print("An unexpected exception was raised")

def ask_password():
    password = getpass.getpass()
    if not is_password_valid(password):
        raise WrongPasswordException()
    return password

def is_password_valid(password):
    return True

if __name__ == "__main__":
    ''' main(sys.argv[1:]) '''
    main("--add site username password".split(" "))
