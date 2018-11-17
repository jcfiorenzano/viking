import argparse


class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-a", "--add", dest="add", nargs=3)
        self.parser.add_argument("-s", "--show", dest="show", nargs=1)

    def parse(self, arg_array):
        return self.parser.parse_args(arg_array)
