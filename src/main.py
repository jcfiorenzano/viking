import getpass
from src.exceptions.Exceptions import WrongPasswordException
from src.argumentParser import ArgumentParser

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
        parsed_object = ArgumentParser().parse(argv)
        password = ask_password()

        if parsed_object.add:
            if len(parsed_object.add) == 3:
                add_password_site(site=parsed_object.add[0], username=parsed_object.add[1], password=parsed_object[2])
            if len(parsed_object.add) == 2:
                new_password = create_password()
                add_password_site(site=parsed_object.add[0], username=parsed_object.add[1], password=new_password)
                print(new_password)
        elif parsed_object.show:
            print()
        elif parsed_object.delete:
            print()

    except Exception:

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
