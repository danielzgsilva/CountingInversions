import argparse
import ast

class Arguments:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Inversion Counting Arguments')

        self.required = self.parser.add_argument_group('required arguments')

        self.required.add_argument('--array',
                                   nargs='+',
                                   help='array for which you would like to count inversions',
                                   required=True)

    def parse(self):
        return self.parser.parse_args()



