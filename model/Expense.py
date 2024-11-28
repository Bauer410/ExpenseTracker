from dataclasses import dataclass


@dataclass
class Category:
    """Class for keeping track of a Category."""
    category_id: int
    category_name: str


@dataclass
class ExpenseDto:
    """Class for keeping track of an Expense."""
    user_id: int
    category: str
    amount: float
    description: str

@dataclass
class ExpenseModel:
    username: str
    category_name: str
    amount: float
    description: str