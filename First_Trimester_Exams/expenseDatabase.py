import os
import uuid
import psycopg
from typing import List, Dict, Any
from dotenv import load_dotenv
from datetime import datetime, timezone

from expense import Expense

# load environment variables
load_dotenv()


class ExpenseDatabase:
    """
    manages a collection of expenses
    """
    def __init__(self):
        """Initializes a list of Expense Instances
        self.expense = expense

        Attributes:
            expense(list): a list to store Expense objects
        """
        # expenses object list
        self.expenses: List[Expense] = []
        
        # Initialize database connection and cursor as context managers
        # Initialize database connection and cursor
        self.connection = psycopg.connect(
            host=os.environ.get('host'),
            port=os.environ.get('port'),
            dbname=os.environ.get('dbname'),
            user=os.environ.get('user'),
            password=os.environ.get('password')
        )
        self.cur = self.connection.cursor() # cursor_factory=psycopg.RealDictCursor

        # Create table if not exists
        self.initialize_table()
    
    
    # Create table
    def initialize_table(self):
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS exams.expense (
                id UUID,
                title VARCHAR(255),
                amount FLOAT,
                created_at TIMESTAMP,
                updated_at TIMESTAMP
            );
            """
        )
    
    
    def add_expense(self, title:str, amount:float):
        """Adds an Expense instance to the database
        """
        expense = Expense(title, amount)
        self.expenses.append(expense)
        
        # Reconnect if the connection is closed
        if self.connection.closed:
            self.connection = psycopg.connect(
                host=os.environ.get('host'),
                port=os.environ.get('port'),
                dbname=os.environ.get('dbname'),
                user=os.environ.get('user'),
                password=os.environ.get('password')
            )
            self.cur = self.connection.cursor()
        
        self.cur.execute(
            """    
            INSERT INTO exams.expense (id, title, amount, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s);
            """,
            (expense.id, expense.title, expense.amount, expense.created_at, expense.updated_at)
            )
        
        self.connection.commit()


    def remove_expense(self, expense_id):
        """Remove an expense from the database
        """
        self.cur.execute(
            """
            DELETE FROM exams.expense
            WHERE exams.expense.id = %s;
            """,
            expense_id
        )
    
        id_s = self.cur.execute(
            """SELECT exams.expense.id
               FROM exams.expense;
            """
        )
        
        # checks if an id exists in the database
        ID = id_s.fetchall()
        if expense_id not in [str(id_) for id_ in ID]:
            print(f"{expense_id} Not In Database")
        
        # Remove from the list
        self.expenses = [expense for expense in self.expenses if str(expense.id) != expense_id]
        
        self.connection.commit()
    
    
    def get_expense_by_id(self, expense_id):
        """fetches an expense by ID from the database
        """
        self.cur.execute(
            """
            SELECT *
            FROM exams.expense
            WHERE exams.expense.id = %s;
            """,
            expense_id
        )
        
        results = self.cur.fetchall()
        
        for expense in results:
            f_expense = {
                'id': str(expense[0]),                 # Convert UUID to string
                'title': expense[1],
                'amount': expense[2],
                'created_at': expense[3].isoformat(),  # Format datetime
                'updated_at': expense[4].isoformat(),  # Format datetime
            }
            print(f_expense)
    
        # check if record exist on database
        id_s = self.cur.execute(
            """SELECT id
               FROM exams.expense;
            """
        )
        
        ID = id_s.fetchall()
        if expense_id not in [str(id_) for id_ in ID]:
            print(f"{expense_id} Not In Database")
        
        self.connection.commit()
    
    
    def get_expense_by_title(self, expense_title) -> List[Dict]:
        """Retrieves expenses by title
        """ 
        
        # actual query
        self.cur.execute(
            """
            SELECT *
            FROM exams.expense
            WHERE title = %s;
            """,
            expense_title
        )
        
        results = self.cur.fetchall()
        
        expenses = [
            {
                'id': str(result[0]),                # Convert UUID to string
                'amount': result[2],
                'created_at': result[3].isoformat(),  # Format datetime
                'updated_at': result[4].isoformat(),  # Format datetime
            }
            for result in results
            ]
        
        # Check if records exist
        if not results:
            print(f"No records found with title: {expense_title}")
        
        return expenses


    def to_dict(self) -> List[Dict]:
        """returns a list of dictionaries representing each expense in the database
        """
        self.cur.execute(
            """
            SELECT *
            FROM exams.expense
            LIMIT 10
            """
        )
        
        instances = self.cur.fetchall()
        
        expenses = [
            {
                'id': str(expense[0]),
                'title': expense[1],
                'amount': expense[2],
                'created_at': expense[3].isoformat(),
                'updated_at': expense[4].isoformat(),
            }
            for expense in instances
        ]
        return expenses

        # re-save the expsenses data to the self.expsenses list after all the operations
        for instance in instances:
            self.expenses.update(expense)
        
    
    def close_connection(self):
        """Closes the database connection and cursor"""
        if not self.connection.closed:
            self.connection.close()
        if not self.cur.closed:
            self.cur.close()
