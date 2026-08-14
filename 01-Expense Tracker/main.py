import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args.echo)

class expense_tracker:

    def init__(self):
        self.expenses = []

    #def add_expense():
