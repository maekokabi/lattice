from expense_manager import ExpenseManager
from note_manager import NoteManager
from task_manager import TaskManager

expense_manager = ExpenseManager()
expense_manager.load_from_file()
note_manager = NoteManager()
note_manager.load_from_file
task_manager = TaskManager()
task_manager.load_from_file()

def run_expense_menu():
    while True:
        print("\nEXPENSE MANAGER")
        print("0- Back")
        print("1- Add expense")
        print("2- Delete expense")
        print("3- Delete expense by id")
        print("4- Search")
        print("5- Display all expenses")

        choice = input("\nWhat do you want to do? ")

        if choice == "1":
            id = int(input("Id: "))
            amount = int(input("Amount: "))
            date = input("Date: ")
            category = input("Category: ")
            necessity = int(input("Necessity: "))
            description = input("Description: ")

            expense_manager.add_expense(id, amount, date, category, necessity, description)

        elif choice == "2":
            id = int(input("Id: "))
            amount = int(input("Amount: "))
            date = input("Date: ")
            category = input("Category: ")
            necessity = int(input("Necessity: "))
            description = input("Description: ")

            expense_manager.delete_expense(id, amount, date, category, necessity, description)

        elif choice == "3":
            expense_id = int(input("\nId: "))

            expense_manager.delete_expense_by_id(expense_id)

        elif choice == "4":
            print("1- Search by category")
            print("2- Search by necessity")
            print("3- Search by date")

            search_choice = input("\nHow do you want to search? ")

            if search_choice == "1":
                category = input("\nSearch category: ")
                expense_manager.search_by_category(category)

            elif search_choice == "2":
                necessity = int(input("\nSearch by necessity: "))
                expense_manager.search_by_necessity(necessity)
            
            elif search_choice == "3":
                date = input("\nSearch by date: ")
                expense_manager.search_by_date(date)
        
        elif choice == "5":
            expense_manager.display_all_expenses()

        elif choice == "0":
            break

        else:
            try:
                print("Wrong input. Try again.")
                run_expense_menu()
            except ValueError as e:
                print(f"{e}")

        





run_expense_menu()

                
