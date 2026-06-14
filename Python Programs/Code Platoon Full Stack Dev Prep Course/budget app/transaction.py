from datetime import date


class Transaction:
    def __init__(self, amount: float, description: str, category: str, trans_date: str = None):
        self.amount = float(amount)
        self.description = description
        self.category = category
        self.date = trans_date or str(date.today())

    def to_dict(self) -> dict:
        return {
            "amount": self.amount,
            "description": self.description,
            "category": self.category,
            "date": self.date,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Transaction":
        return cls(
            amount=data["amount"],
            description=data["description"],
            category=data["category"],
            trans_date=data["date"],
        )

    def __repr__(self) -> str:
        return f"Transaction({self.date} | {self.category} | {self.description} | ${self.amount:.2f})"
