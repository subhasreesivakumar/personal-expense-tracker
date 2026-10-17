
# Personal Expense Tracker
# Created by Subhasree S.

expenses = []

print("===== PERSONAL EXPENSE TRACKER =====")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter expense name: ")

        try:
            amount = float(input("Enter amount (Rs.): "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            expenses.append({
                "item": item,
                "amount": amount
            })
            print("Expense added successfully!")

        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\n--- Your Expenses ---")
            for i, expense in enumerate(expenses, start=1):
                print(
                    f"{i}. {expense['item']} - "
                    f"Rs. {expense['amount']:.2f}"
                )

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total Expenses: Rs. {total:.2f}")

    elif choice == "4":
        print("Thank you for using the Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
