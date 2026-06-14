import csv
import os
from typing import List

BUDGET_FILE = os.path.join(os.path.dirname(__file__), "data", "budget.csv")
TRANSACTIONS_FILE = os.path.join(os.path.dirname(__file__), "data", "transactions.csv")


class CSVHandler:
    @staticmethod
    def ensure_data_dir():
        os.makedirs(os.path.dirname(BUDGET_FILE), exist_ok=True)

    # --- Budget / income ---

    @staticmethod
    def load_budget() -> dict:
        """Returns {'income': float, 'categories': [{'name': str, 'monthly_limit': float}]}"""
        CSVHandler.ensure_data_dir()
        data = {"income": 0.0, "categories": []}
        if not os.path.exists(BUDGET_FILE):
            return data
        with open(BUDGET_FILE, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["type"] == "income":
                    data["income"] = float(row["value"])
                elif row["type"] == "category":
                    data["categories"].append(
                        {"name": row["name"], "monthly_limit": float(row["value"])}
                    )
        return data

    @staticmethod
    def save_budget(income: float, categories: list):
        CSVHandler.ensure_data_dir()
        with open(BUDGET_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["type", "name", "value"])
            writer.writeheader()
            writer.writerow({"type": "income", "name": "income", "value": income})
            for cat in categories:
                writer.writerow(
                    {"type": "category", "name": cat["name"], "value": cat["monthly_limit"]}
                )

    # --- Transactions ---

    @staticmethod
    def load_transactions() -> List[dict]:
        CSVHandler.ensure_data_dir()
        if not os.path.exists(TRANSACTIONS_FILE):
            return []
        with open(TRANSACTIONS_FILE, newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)

    @staticmethod
    def save_transactions(transactions: list):
        CSVHandler.ensure_data_dir()
        if not transactions:
            with open(TRANSACTIONS_FILE, "w", newline="") as f:
                writer = csv.DictWriter(
                    f, fieldnames=["amount", "description", "category", "date"]
                )
                writer.writeheader()
            return
        with open(TRANSACTIONS_FILE, "w", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["amount", "description", "category", "date"]
            )
            writer.writeheader()
            for t in transactions:
                writer.writerow(t)

    @staticmethod
    def append_transaction(transaction_dict: dict):
        CSVHandler.ensure_data_dir()
        file_exists = os.path.exists(TRANSACTIONS_FILE)
        with open(TRANSACTIONS_FILE, "a", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["amount", "description", "category", "date"]
            )
            if not file_exists:
                writer.writeheader()
            writer.writerow(transaction_dict)
