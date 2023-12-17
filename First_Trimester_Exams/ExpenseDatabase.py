#!/usr/bin/env python

"""
Manages a collection of Expense Objects
"""

import uuid
from expense import Expense
from datetime import datetime, timezone
from typing import int, List, float, Dict

class ExpenseDatabase(Expense):
    """_summary_
    """
    def __init__(self, expense):
        """Initializes a list of Expense Instances

        Attributes:
            expense(list): a list of Epense instances
        """
        self.expense = expense
    
    
    def add_expense(self, expense):
        """Adds an Expense instance to the database
        """
    
    
    def remove_expense(self, expense_id):
        """Remove an expense from the database
        """
    
    
    def get_expense_by_id(self, expense_id):
        """fetches an expense by ID from the database
        """
    
    
    def get_expense_by_title(self, expense_title):
        """Retrieves an expense by title from the database
        """
    
    
    def to_dict(self) -> Dict:
        """_summary_
        """