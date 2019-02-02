import sys
import os
import argparse
import colorama
import viking.handle.handle_factory as HandleFactory
import viking.util.print_utils as print_utils
from viking.exceptions.exception import UserNotAuthenticateException
from viking.exceptions.exception import WrongPasswordException
from viking.exceptions.exception import SiteNotFound


def parsed_arguments(argv):
    if argv is None or len(argv) == 0:
        argv = ["-s"]
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
                        help='Show the information of a given site with its questions if any, if not site is provided then show all sites registered except for questions')

    parser.add_argument("-d", "--delete",
                        dest="delete",
                        nargs=1,
                        metavar='site',
                        help='Remove a given site')

    return parser.parse_args(argv)


def main(argv):
    colorama.init()

    try:
        parsed_object = parsed_arguments(argv)

        command_handle = HandleFactory.create_handle(parsed_object)
        command_handle.handle()

    except WrongPasswordException:
        print(print_utils.error_format("Password incorrect"))
    except UserNotAuthenticateException:
        print(print_utils.error_format("Fail to authenticate the user."))
    except SiteNotFound as e:
        print(print_utils.error_format("The site {0} was not found.".format(e)))
    finally:
        colorama.deinit()

def _is_root():
    return os.getuid() == 0

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
