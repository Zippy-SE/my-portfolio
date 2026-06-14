from budget import Budget


class CLI:
    DIVIDER = "-" * 50

    def __init__(self):
        self.budget = Budget()

    def run(self):
        self._print_welcome()
        while True:
            self._print_main_menu()
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self._view_summary()
            elif choice == "2":
                self._add_transaction()
            elif choice == "3":
                self._update_income()
            elif choice == "4":
                self._set_category_limit()
            elif choice == "5":
                self._add_category()
            elif choice == "6":
                self._view_transactions()
            elif choice == "7":
                self._view_category_detail()
            elif choice == "q":
                print("\nGoodbye! Budget saved.\n")
                break
            else:
                print("  Invalid option. Try again.")

    # --- Menus ---

    def _print_welcome(self):
        print("\n" + "=" * 50)
        print("        BUDGET TRACKER")
        print("=" * 50)
        if self.budget.income == 0:
            print("  Tip: Set your monthly income to get started.")

    def _print_main_menu(self):
        print(f"\n{self.DIVIDER}")
        print("  MAIN MENU")
        print(self.DIVIDER)
        print("  1. View budget summary")
        print("  2. Add transaction")
        print("  3. Update monthly income")
        print("  4. Set category spending limit")
        print("  5. Add new category")
        print("  6. View all transactions")
        print("  7. View transactions by category")
        print("  q. Quit")
        print(self.DIVIDER)

    # --- Actions ---

    def _view_summary(self):
        print(f"\n{self.DIVIDER}")
        print("  MONTHLY BUDGET SUMMARY")
        print(self.DIVIDER)
        print(f"  Monthly Income:  ${self.budget.income:>10.2f}")
        print(f"  Total Spent:     ${self.budget.total_spent():>10.2f}")
        remaining_income = self.budget.income - self.budget.total_spent()
        print(f"  Remaining:       ${remaining_income:>10.2f}")
        print()
        print(f"  {'Category':<12} {'Limit':>8} {'Spent':>8} {'Left':>8} {'% Income':>9}")
        print(f"  {'-'*12} {'-'*8} {'-'*8} {'-'*8} {'-'*9}")
        for row in self.budget.monthly_cost_summary():
            left = row["remaining"]
            flag = " !" if left < 0 else ""
            print(
                f"  {row['category']:<12} "
                f"${row['limit']:>7.2f} "
                f"${row['spent']:>7.2f} "
                f"${left:>7.2f} "
                f"{row['pct_of_income']:>8.1f}%"
                f"{flag}"
            )
        print(self.DIVIDER)

    def _add_transaction(self):
        print(f"\n{self.DIVIDER}")
        print("  ADD TRANSACTION")
        print(self.DIVIDER)
        print("  Categories:", ", ".join(self.budget.category_names()))
        category = input("  Category: ").strip()
        if not self.budget.get_category(category):
            print(f"  Error: '{category}' is not a valid category.")
            return
        description = input("  Description: ").strip()
        amount_str = input("  Amount ($): ").strip()
        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError
        except ValueError:
            print("  Error: Amount must be a positive number.")
            return
        t = self.budget.add_transaction(amount, description, category)
        print(f"\n  ✓ Added: {t.description} — ${t.amount:.2f} to {t.category}")
        remaining = self.budget.remaining_in(category)
        if remaining < 0:
            print(f"  Warning: You are ${abs(remaining):.2f} over budget in {category}!")
        else:
            print(f"  Remaining in {category}: ${remaining:.2f}")

    def _update_income(self):
        print(f"\n{self.DIVIDER}")
        print("  UPDATE MONTHLY INCOME")
        print(self.DIVIDER)
        print(f"  Current income: ${self.budget.income:.2f}")
        amount_str = input("  New monthly income ($): ").strip()
        try:
            amount = float(amount_str)
            if amount < 0:
                raise ValueError
        except ValueError:
            print("  Error: Income must be a non-negative number.")
            return
        self.budget.set_income(amount)
        print(f"  ✓ Monthly income updated to ${amount:.2f}")

    def _set_category_limit(self):
        print(f"\n{self.DIVIDER}")
        print("  SET CATEGORY SPENDING LIMIT")
        print(self.DIVIDER)
        print("  Categories:", ", ".join(self.budget.category_names()))
        category = input("  Category: ").strip()
        if not self.budget.get_category(category):
            print(f"  Error: '{category}' is not a valid category.")
            return
        limit_str = input(f"  Monthly limit for {category} ($): ").strip()
        try:
            limit = float(limit_str)
            if limit < 0:
                raise ValueError
        except ValueError:
            print("  Error: Limit must be a non-negative number.")
            return
        self.budget.set_category_limit(category, limit)
        print(f"  ✓ Limit for {category} set to ${limit:.2f}")

    def _add_category(self):
        print(f"\n{self.DIVIDER}")
        print("  ADD NEW CATEGORY")
        print(self.DIVIDER)
        name = input("  Category name: ").strip()
        if not name:
            print("  Error: Name cannot be empty.")
            return
        limit_str = input(f"  Monthly limit for {name} ($, or 0 to set later): ").strip()
        try:
            limit = float(limit_str)
            if limit < 0:
                raise ValueError
        except ValueError:
            print("  Error: Limit must be a non-negative number.")
            return
        try:
            self.budget.add_category(name, limit)
            print(f"  ✓ Category '{name}' added with limit ${limit:.2f}")
        except ValueError as e:
            print(f"  Error: {e}")

    def _view_transactions(self):
        print(f"\n{self.DIVIDER}")
        print("  ALL TRANSACTIONS")
        print(self.DIVIDER)
        if not self.budget.transactions:
            print("  No transactions yet.")
            return
        print(f"  {'Date':<12} {'Category':<12} {'Amount':>8}  Description")
        print(f"  {'-'*12} {'-'*12} {'-'*8}  {'-'*20}")
        for t in self.budget.transactions:
            print(f"  {t.date:<12} {t.category:<12} ${t.amount:>7.2f}  {t.description}")
        print(f"\n  Total: ${self.budget.total_spent():.2f}")
        print(self.DIVIDER)

    def _view_category_detail(self):
        print(f"\n{self.DIVIDER}")
        print("  TRANSACTIONS BY CATEGORY")
        print(self.DIVIDER)
        print("  Categories:", ", ".join(self.budget.category_names()))
        category = input("  Category: ").strip()
        if not self.budget.get_category(category):
            print(f"  Error: '{category}' is not a valid category.")
            return
        transactions = self.budget.transactions_for(category)
        cat = self.budget.get_category(category)
        spent = self.budget.spent_in(category)
        pct = self.budget.percent_of_income(category)
        print(f"\n  {category}  |  Limit: ${cat.monthly_limit:.2f}  |  Spent: ${spent:.2f}  |  {pct:.1f}% of income")
        print()
        if not transactions:
            print("  No transactions in this category.")
        else:
            print(f"  {'Date':<12} {'Amount':>8}  Description")
            print(f"  {'-'*12} {'-'*8}  {'-'*20}")
            for t in transactions:
                print(f"  {t.date:<12} ${t.amount:>7.2f}  {t.description}")
        remaining = self.budget.remaining_in(category)
        if remaining < 0:
            print(f"\n  ⚠  Over budget by ${abs(remaining):.2f}")
        else:
            print(f"\n  Remaining budget: ${remaining:.2f}")
        print(self.DIVIDER)
