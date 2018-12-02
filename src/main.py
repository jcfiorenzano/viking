import sys
from src.exceptions.Exceptions import UserNotAuthenticateException
from src.exceptions.Exceptions import WrongPasswordException
from src.argumentParser.ArgumentParser import ArgumentParser
from src.handle.HandleFactory import HandleFactory

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
# Todo: Instead of copy the password directly in the command line is more secure if the password is passed with getPass when we are going to add a new site
# Todo: Encrypt the whole file
# Todo: create unit testing
# Todo: Create a command to get the version number
# Todo: Create a structure that can handle more than password, example pins or secure questions


def main(argv):

    try:
        parser = ArgumentParser()
        parsed_object = parser.parse(argv)

        command_handle = HandleFactory.create_handle(parsed_object)
        command_handle.handle()

    except WrongPasswordException:
        print("Password incorrect")
    except UserNotAuthenticateException:
        print("Fail to authenticate the user")
    # except Exception:
    #    print("An unexpected exception was raised")


if __name__ == "__main__":
     main(sys.argv[1:])
    # main("-a asd asd asd".split())
    # main("-s asd".split())
    # main("-d asd".split())
    # main("-s asd".split())
    # main("-a bcb bcb bcb".split())
    # main("-h".split())

