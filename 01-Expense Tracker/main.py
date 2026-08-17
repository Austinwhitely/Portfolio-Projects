
from argparse import ArgumentParser, Namespace
from datetime import date
import calendar as cal
import csv



# Created ExpenseTracker class to encapsulate applications function.
class ExpenseTracker:

    # Creates expense list alongside each header when ExpenseTracker is constructed
    def __init__(self):
        self.expense_list = [["ID", "Date", "Description", "Amount"]]  
          
    
    # Functions for each command 
    def addition_func(self,args):
        self.expense_list.append([len(self.expense_list), date.today(), args.description , args.amount])

    def list_func(self,args):
        
        # Exports data to a csv file when given the command
        if args.export:
            
            with open("data.csv","w") as f:
                writer = csv.writer(f)
                writer.writerow(self.expense_list[0])
                writer.writerows(self.expense_list[1:])
                
        # If not given export command it lists entries in the terminal        
        else:
            print("\t".join(self.expense_list[0]))
            for row in self.expense_list[1:]:
                formatted_row = [row[0],
                                row[1],
                                row[2],
                                f"${row[3]:.2f}"]  
               
                print(("\t".join(map(str,formatted_row))))

    def summary_func(self,args):
        total = 0.0

        # Sums up total expenses for a given month 
        if args.month != None and 1<= args.month <=12:
            print (f"this is the expenses for {cal.month_name[args.month]}")
            
            for row in self.expense_list[1:]:
                    
                    if row[1].month == args.month:
                        total += row[3] 
                    elif row[1].month > args.month:
                        break            
                                
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
        

    # All of the parser logic in one function
    def parser_controller(self,input):

        parser = ArgumentParser(description= "Expense Tracker")
        subparser = parser.add_subparsers(dest="command", help="Expense tracker")
        self.setup_addition_parser(subparser)   
        self.setup_delete_parser(subparser)
        self.setup_list_parser(subparser)
        self.setup_summary_parser(subparser)
        try:
            return parser.parse_args(input)
        except SystemExit:
            return None   
        
    # Creating all of the commands 
    def setup_addition_parser(self,parser):
        
        addition_parser = parser.add_parser("add", help='Adds expense to list')
        addition_parser.add_argument("--description", type= str, required=True,help="Description of expense in a string", dest= "description")
        addition_parser.add_argument("--amount", type= float, required=True, help= "Cost of expense in dollars", dest= "amount")
        addition_parser.set_defaults(func=self.addition_func)
    
    def setup_list_parser(self,parser):
        list_parser = parser.add_parser("list", help="Lists out all entries")
        list_parser.add_argument("--export",action="store_true", help="Prints out a CSV of all entries",dest="export")
        list_parser.set_defaults(func=self.list_func)

    def setup_summary_parser(self,parser):
        summary_parser = parser.add_parser("summary", help="Lists total of all expenses")
        summary_parser.add_argument("--month", type= int, required=False, help="Gives a summary of the expenses for the month that is entered", dest= "month")
        summary_parser.set_defaults(func=self.summary_func)

    def setup_delete_parser(self,parser):
        delete_parser = parser.add_parser("delete", help="Deletes entry for entered ID")
        delete_parser.add_argument("--id", type= int, required=False, help="Takes int for the ID that you want to remove", dest="id")
        delete_parser.add_argument("--removed",action= "store_true",required=False, help="Returns the last deleted entry")
        delete_parser.set_defaults(func=self.delete_func)

# Loops until the user enters the exit command
def main():
    
    et = ExpenseTracker()
    while True:
        user_input = input("Expense Tracker: ")
        if user_input.lower() == "exit":
                        break
        args: Namespace = et.parser_controller(user_input.split())
        
        
        try: args.func(args)
        except:
            print("This is not a command")
       
if __name__ == "__main__":
    main()
    

