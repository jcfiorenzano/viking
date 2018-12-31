import sys
import argparse
import viking.handle.handle_factory as HandleFactory
from viking.exceptions.exception import UserNotAuthenticateException
from viking.exceptions.exception import WrongPasswordException


def parsed_arguments(argv):
    parser = argparse.ArgumentParser(description="Password manager tool")
    parser.add_argument("-a", "--add",
                        dest="add",
                        nargs=2,
                        metavar=('site', 'username'),
                        help='Store a new site')

    parser.add_argument("-s", "--show",
                        dest="show",
                        nargs='?',
                        const=[],
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


if __name__ == "__main__":
     main(sys.argv[1:])
    # main("-a site username".split())
    # main("-s site".split())
    # main("-s si".split())
    # main("-s".split())
    # main("-d site".split())
    # main("-s site".split())
    # main("-a site2 username2".split())
    # main("-a site2 username3".split())
    # main("-s site2".split())
    # main("-a site2 username4".split())
    # main("-s site2".split())
    # main("-h".split())
