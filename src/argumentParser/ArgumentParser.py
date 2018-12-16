import argparse


class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Password manager tool")
        self.parser.add_argument("-a", "--add",
                                 dest="add",
                                 nargs=2,
                                 metavar=('site', 'username'),
                                 help='Store a new site')

        self.parser.add_argument("-s", "--show",
                                 dest="show",
                                 nargs=1,
                                 metavar='[site]',
                                 help='Show the information of a given site, if not site is provided then show all')

        self.parser.add_argument("-d", "--delete",
                                 dest="delete",
                                 nargs=1,
                                 metavar='site',
                                 help='Remove a given site')

    def parse(self, arg_array):
        return self.parser.parse_args(arg_array)
