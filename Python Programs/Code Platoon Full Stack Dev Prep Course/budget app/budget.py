from budget_category import BudgetCategory
from transaction import Transaction
from csv_handler import CSVHandler
from typing import List


class Budget:
    def __init__(self):
        self.income: float = 0.0
        self.categories: List[BudgetCategory] = []
        self.transactions: List[Transaction] = []
        self._load()

    # --- Persistence ---

    def _load(self):
        data = CSVHandler.load_budget()
        self.income = data["income"]
        if data["categories"]:
            self.categories = [BudgetCategory.from_dict(c) for c in data["categories"]]
        else:
            self.categories = [BudgetCategory(name) for name in BudgetCategory.DEFAULT_CATEGORIES]

        raw_transactions = CSVHandler.load_transactions()
        self.transactions = [Transaction.from_dict(t) for t in raw_transactions]

    def save(self):
        CSVHandler.save_budget(self.income, [c.to_dict() for c in self.categories])
        CSVHandler.save_transactions([t.to_dict() for t in self.transactions])

    # --- Income ---

    def set_income(self, amount: float):
        self.income = float(amount)
        self.save()

    # --- Categories ---

    def category_names(self) -> List[str]:
        return [c.name for c in self.categories]

    def get_category(self, name: str) -> BudgetCategory:
        for cat in self.categories:
            if cat.name.lower() == name.lower():
                return cat
        return None

    def add_category(self, name: str, monthly_limit: float = 0.0):
        if self.get_category(name):
            raise ValueError(f"Category '{name}' already exists.")
        self.categories.append(BudgetCategory(name, monthly_limit))
        self.save()

    def set_category_limit(self, name: str, limit: float):
        cat = self.get_category(name)
        if not cat:
            raise ValueError(f"Category '{name}' not found.")
        cat.monthly_limit = float(limit)
        self.save()

    # --- Transactions ---

    def add_transaction(self, amount: float, description: str, category: str) -> Transaction:
        if not self.get_category(category):
            raise ValueError(f"Category '{category}' not found.")
        t = Transaction(amount, description, category)
        self.transactions.append(t)
        CSVHandler.append_transaction(t.to_dict())
        return t

    def transactions_for(self, category: str) -> List[Transaction]:
        return [t for t in self.transactions if t.category.lower() == category.lower()]

    # --- Calculations ---

    def total_spent(self) -> float:
        return sum(t.amount for t in self.transactions)

    def spent_in(self, category: str) -> float:
        return sum(t.amount for t in self.transactions_for(category))

    def remaining_in(self, category: str) -> float:
        cat = self.get_category(category)
        if not cat:
            return 0.0
        return cat.monthly_limit - self.spent_in(category)

    def percent_of_income(self, category: str) -> float:
        if self.income == 0:
            return 0.0
        return (self.spent_in(category) / self.income) * 100

    def monthly_cost_summary(self) -> List[dict]:
        summary = []
        for cat in self.categories:
            spent = self.spent_in(cat.name)
            summary.append(
                {
                    "category": cat.name,
                    "limit": cat.monthly_limit,
                    "spent": spent,
                    "remaining": cat.monthly_limit - spent,
                    "pct_of_income": self.percent_of_income(cat.name),
                }
            )
        return summary
