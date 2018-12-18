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
        
        -a site username
        
        
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
   #     print("An unexpected exception was raised")


if __name__ == "__main__":
     main(sys.argv[1:])
    # main("-a asd asd".split())
    # main("-s asd".split())
    # main("-d asd".split())
    # main("-s asd".split())
    # main("-a bcb bcb".split())
    # main("-h".split())

