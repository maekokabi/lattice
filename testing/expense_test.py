from src.expense_manager import Expense, ExpenseManager

tracker = ExpenseManager()
expense1 = Expense(1, 50, "2025-04-12", "food", "not important", "lunch")
expense2 = Expense(2, 100, "2023-03-23", "clothes", "urgent", "winter clothes")


tracker.add_expense(expense1)
tracker.add_expense(expense2)

# tracker.save_to_file()

# old_tracker = ExpenseManager()
# old_tracker.load_from_file()
# old_tracker.display_all_expenses()

# tracker.delete_expense(expense1)
# tracker.display_all_expenses()

tracker.delete_expense_by_id(2)
tracker.display_all_expenses()
