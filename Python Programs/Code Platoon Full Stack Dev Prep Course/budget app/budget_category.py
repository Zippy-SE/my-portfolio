class BudgetCategory:
    DEFAULT_CATEGORIES = ["Living", "Food", "Travel", "Savings", "Leisure"]

    def __init__(self, name: str, monthly_limit: float = 0.0):
        self.name = name
        self.monthly_limit = float(monthly_limit)

    def to_dict(self) -> dict:
        return {"name": self.name, "monthly_limit": self.monthly_limit}

    @classmethod
    def from_dict(cls, data: dict) -> "BudgetCategory":
        return cls(name=data["name"], monthly_limit=float(data["monthly_limit"]))

    def __repr__(self) -> str:
        return f"BudgetCategory({self.name}, limit=${self.monthly_limit:.2f})"
