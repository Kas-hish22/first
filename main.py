from expenses import add_expense, view_expenses, generate_summary

def menu():
    while True:
        print("\n Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Generate Summary Report")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category (Food, Travel, Bills, etc.): ")
            desc = input("Optional description: ")
            add_expense(amount, category, desc)
            print(" Expense added.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            generate_summary()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
