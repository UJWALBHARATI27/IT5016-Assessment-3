"""
improving the code by adding class

"""

""" ANSI color codes """
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"

class RequisitionSystem:
    counter_id = 10000  
    requisitions = []    # a list to store all the dictionary

    def __init__(me):
        RequisitionSystem.counter_id += 1
        me.requisition_id = RequisitionSystem.counter_id

        # collects user data and loops to check if the entered item is correct or not
        # adding all the function in a single method from previous 
        # added K.I.S.S to keep it clear and simple by collecting input and lopping it to see data and error validation
        # used DRY by reusing logic pattern for input validation
        while True:
            me.date = input("Enter the date (yyyy-mm-dd): ")
            if me.date.strip() == "":
                print("You have entered nothing, Please enter a valid date.")
            else:
                break
        while True:
            me.staff_id = input("Enter your Staff ID (letters followed by 4 numbers): ")
            if me.staff_id.strip() == "":
                print("You have entered nothing' Please enter a valid Staff ID.")
            else:
                break
        while True:
            me.staff_name = input("Enter your name: ")
            if me.staff_name.strip() == "":
                print("You have entered nothing, Please enter your name.")
            else:
                break
        print(f"""{ITALIC}{BLINK}{LIGHT_RED}
====ITEM LIST===={END}
{GREEN}
Name         Price{END}
{LIGHT_PURPLE}
Coffee--------$200
Paper---------$100
Pen-----------$50{END}
""")
    # adding a loop with try and except where it checks error validation of items 
    # used SRP only handles input number of items
        while True:
            try:
                num_item = int(input("How many items do you want? "))
                if num_item < 0:
                    print("Please enter a positive number")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")
# to calculate the total price of the items used SRP only handles calculation about total price
        me.total_price = 0.00

        for x in range(num_item):
            while True:
                item_name = input(f"Enter the name of item {x+1}: ")
                if item_name.strip() == "":
                    print("You have entered nothing. Please enter the item name.")
                else:
                    break
            while True:
                try:
                    item_price = float(input(f"Enter the price of {item_name}: "))
                    if item_price < 0:
                        print("Please enter a positive number.")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number.")

            me.total_price += item_price

# condition where if the total number is less or higher than
# added Y.A.G.N.I and Clean Code used simple approval logic without unnecessary complexity
        if me.total_price < 500:
            me.status = "approved"
            me.refrence_number = me.staff_id.upper() + str(me.requisition_id)[-3:]
        else:
            me.status = "Pending"
            me.refrence_number = "On process"


# saving all the requisition in a list
        RequisitionSystem.requisitions.append(me)

# creating a method to respond to requisitions by manager
    def respond_requisition(me, response):
        req = response.lower()
        if req == "approved":
            me.status = "approved"
            me.refrence_number = me.staff_id.upper() + str(me.requisition_id)[-3:]
        elif req == "not approved":
            me.status = "not approved"
            me.refrence_number = "not available"
        else:
            print("Your response is invalid. Please enter 'approved' or 'not approved'.")\
            
# A Class method for displaying all the info stored on a object
    def display_all():
        if not RequisitionSystem.requisitions:
            print("No requisitions submitted yet.")
            return
        print(f"{CYAN}=== All Requisitions ==={END}")
        for req in RequisitionSystem.requisitions:
            print(f"""{BOLD}{UNDERLINE}{RED}
Date: {req.date}
Requisition ID: {req.requisition_id}
Staff ID: {req.staff_id}
Staff Name: {req.staff_name}
Total: ${req.total_price:.2f}
Status: {req.status}
Approval Reference Number: {req.refrence_number} {END}
""")

# to display all the statictics used SRP only displays statistics
    def statistics():
        total = len(RequisitionSystem.requisitions)

        approved = 0
        pending = 0
        not_approved = 0

    # used Clean Code > Clever Code: looping the requsition and counting according to statuts
        for i in RequisitionSystem.requisitions:
            if i.status == "approved":
                approved += 1
            elif i.status == "pending":
                pending += 1
            elif i.status == "not approved":
                not_approved += 1

        print(f"""{BOLD}{UNDERLINE}{RED}
=== Requisition Statistics ===
Total requisitions submitted: {total}
Total approved requisitions: {approved}
Total pending requisitions: {pending}
Total not approved requisitions: {not_approved}{END}""")


# adding menu function to make the code easy to ascess and control specfic function 
# used separation of concerns it runs individual methods if promted
def menu():
    while True:
        print(f"""{CYAN}
========= Requisition System =========
1. Create a new requisition
2. Display all requisitions
3. Display statistics
4. Manager response
5. Exit{END}
""")
        num_choice = input("Choose a number from 1 to 5: ").strip()

        if num_choice == "1":
            req = RequisitionSystem()
            print("Requisition is created successfully!!!!")
        elif num_choice == "2":
            if RequisitionSystem.requisitions:
                RequisitionSystem.display_all()
            else:
                print("Requisitions not found.")
        elif num_choice == "3":
            if RequisitionSystem.requisitions:
                RequisitionSystem.statistics()
            else:
                print("Requisitions not found.")
        elif num_choice == "4":
            if not RequisitionSystem.requisitions:
                print("No requisitions available.")
                continue
            try:
                req_id = int(input("Enter requisition ID: "))
            except ValueError:
                print("Please enter a number")
                continue
            for req in RequisitionSystem.requisitions:
                if req.requisition_id == req_id:
                    response = input("Enter response (approved/not approved): ")
                    req.respond_requisition(response)
                    print("Response recorded.")
                    break
            else:
                print("No requisition found")
        elif num_choice == "5":
            print("Exiting")
            break
        else:
            print("your choice is invalid, please enter a number between 1 and 5.")
if __name__ == "__main__":
    menu()
