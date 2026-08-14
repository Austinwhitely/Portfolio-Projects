
from argparse import ArgumentParser, Namespace
ID = 1
expense_list = [["ID", "Date", "Description", "Amount"]]

def main():

    parser = ArgumentParser(description= "Expense Tracker")
    subparser = parser.add_subparsers(dest="command", help=" expense tracker")

    addition_parser = subparser.add_parser("add", help=' adds expense to list')
    addition_parser.add_argument("--description", type= str, required=True,help="Description of expense in a string")
    addition_parser.add_argument("--amount", type= float, required=True, help= "cost of expense in dollars")
    addition_parser.set_defaults(func=addition_func)

    list_parser = subparser.add_parser("list", help="lists out all expenses")
    list_parser.set_defaults(func=list_func)
                                
    # a namespace to call all of my arguments
    args: Namespace = parser.parse_args()
    args.func(args)

def addition_func(args):
 expense_list.append([ID, "01/20/10", "games", 10.0])

def list_func(args):
   for row in expense_list:
      print("\t".join(row)) 

 


if __name__ == "__main__":
    main()
    

