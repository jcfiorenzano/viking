import sys
import argparse
import src.handle.HandleFactory as HandleFactory
from src.exceptions.Exceptions import UserNotAuthenticateException
from src.exceptions.Exceptions import WrongPasswordException

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


def parsed_arguments(argv):
    parser = argparse.ArgumentParser(description="Password manager tool")
    parser.add_argument("-a", "--add",
                             dest="add",
                             nargs=2,
                             metavar=('site', 'username'),
                             help='Store a new site')

    parser.add_argument("-s", "--show",
                             dest="show",
                             nargs=1,
                             metavar='[site]',
                             help='Show the information of a given site, if not site is provided then show all')

    parser.add_argument("-d", "--delete",
                             dest="delete",
                             nargs=1,
                             metavar='site',
                             help='Remove a given site')

    return parser.parse_args(argv)


def main(argv):

    try:
        parsed_object = parsed_arguments(argv)

        command_handle = HandleFactory.create_handle(parsed_object)
        command_handle.handle()

    except WrongPasswordException:
        print("Password incorrect")
    except UserNotAuthenticateException:
        print("Fail to authenticate the user")
    except Exception:
        print("An unexpected exception was raised")


if __name__ == "__main__":
     main(sys.argv[1:])
    # main("-a asd asd".split())
    # main("-s asd".split())
    # main("-d asd".split())
    # main("-s asd".split())
    # main("-a bcb bcb".split())
    # main("-h".split())

