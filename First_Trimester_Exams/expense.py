#!/usr/bin/env python

"""
A distinct representation and a collection of financial expenses
"""

import os
import uuid
import psycopg
from typing import List, Dict
from dotenv import load_dotenv
from datetime import datetime, timezone

# load environment variables
load_dotenv()

class Expense:
    """creates and expense object
    """
    def __init__(self, title:str, amount:float):
        """Initializes the attributes upon which other methods will depend

        Attributes:
            id (uuid string): a unique identifier
            title (string): this represents the title of the expense
            amount (float): this represents an expense amount
            
        id (uuid string): a unique identifier    
        created_at (timestamp): marks when an expense is created IN UTC
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = self._timestamp().isoformat()
        self.updated_at = self._timestamp().isoformat()
        
        
    def update(self, title:str=None, amount:float=None):
        """
        - This method allows for updating the `title` and(or) the `amount`
        - By updating the `updated_at` timestamp
        - updated_at (timestamp): marks when an expense is updated IN UTC
        """
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
            
        self.updated_at = self._timestamp()
    
    
    def to_dict(self) -> Dict:
        """Returns a dictionary representation of the expense
        """
        expense_dict = {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }
        
        return expense_dict
        

    def _timestamp(self):
        """returns the timestamp when called

        Returns:
            timestamp: returns as a timezone-aware timestamp
        """
        # return datetime.utcnow().astimezone()
        return datetime.now(timezone.utc)
