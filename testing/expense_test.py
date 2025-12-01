from src.expense_manager import Expense, ExpenseManager

tracker = ExpenseManager()
expense1 = Expense(1, 50, "2025-04-12", 98, "not important", "lunch")
expense2 = Expense(2, 100, "20231", 76, "urgent", "winter clothes")


tracker.add_expense(expense1)
tracker.add_expense(expense2)

# tracker.save_to_file()

# old_tracker = ExpenseManager()
# old_tracker.load_from_file()
# old_tracker.display_all_expenses()
