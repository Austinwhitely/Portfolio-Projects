
from argparse import ArgumentParser, Namespace
from datetime import date


# Created ExpenseTracker class to encapsulate applications function.
class ExpenseTracker:

    # Creates expense list alongside each header when ExpenseTracker is constructed
    def __init__(self):
        self.expense_list = [["ID", "Date", "Description", "Amount"]]  
          
    
    # Functions for each command 
    def addition_func(self,args):
        self.expense_list.append([len(self.expense_list), date.today(), args.description , args.amount])

    def list_func(self,args):
        print("\t".join(self.expense_list[0]))

        for row in self.expense_list[1:]:
         formatted_row = [row[0],
                          row[1],
                          row[2],
                          f"${row[3]:.2f}"]
         
         print(("\t".join(map(str,formatted_row))))

    def summary_func(self,args):
        total = 0.0

        #Placeholder logic for listing expense for entered month
        if args.month != None:
            print ("this is the month")
            for row in self.expense_list[1:]:
                        total += row[3]
            print(f"${total:.2f}") 

        else:    
            for row in self.expense_list[1:]:
                total += row[3]
            print(f"${total}")  

    def delete_func(self,args):
        # Deletes entry for the ID that is entered, updates the remaining ID's, and stores the last deleted entry
        if args.command == "--id":    
                    recently_deleted = self.expense_list.pop(args.id)
                    for row in self.expense_list[1:]:
                        row[0] =  self.expense_list.index(row)
                        print(("\t".join(map(str,row))))
        try: 
            args.command == "removed"
            print(recently_deleted) 
        except UnboundLocalError:
            print("There is no recently deleted entry")
        

    # All of the parsers in one function 
    def all_parsers(self,input):

        parser = ArgumentParser(description= "Expense Tracker")
        subparser = parser.add_subparsers(dest="command", help=" expense tracker")

        addition_parser = subparser.add_parser("add", help=' adds expense to list')
        addition_parser.add_argument("--description", type= str, required=True,help="Description of expense in a string", dest= "description")
        addition_parser.add_argument("--amount", type= float, required=True, help= "cost of expense in dollars", dest= "amount")
        addition_parser.set_defaults(func=self.addition_func)

        list_parser = subparser.add_parser("list", help="lists out all entries")
        list_parser.set_defaults(func=self.list_func)

        summary_parser = subparser.add_parser("summary", help="Lists total of all expenses")
        summary_parser.add_argument("--month", type= int, required=False, help="Gives a summary of the expenses for the month that is entered", dest= "month")
        summary_parser.set_defaults(func=self.summary_func)

        delete_parser = subparser.add_parser("delete", help="lists out all expenses")
        delete_parser.add_argument("--id", type= int, required=False, help="Deletes entry for entered ID", dest="id")
        delete_parser.add_argument("--removed",action= "store_true",required=False, help="Returns the last deleted entry")
        delete_parser.set_defaults(func=self.delete_func)

        try:
            return parser.parse_args(input)
        except SystemExit:
            return None
        
# Loops until the user enters the exit command
def main():
    et = ExpenseTracker()
    while True:
        user_input = input("Expense Tracker: ")
        if user_input.lower() == "exit":
                        break
        args: Namespace = et.all_parsers(user_input.split())
        
        
        args.func(args)
       



if __name__ == "__main__":
    main()
    

