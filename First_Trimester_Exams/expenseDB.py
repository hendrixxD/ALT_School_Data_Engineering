import os
import uuid
import psycopg
from typing import List, Dict
from dotenv import load_dotenv
from datetime import datetime, timezone

from expense import Expense

# load environment variables
load_dotenv()


class ExpenseDB:
    """
    manages a collection of expenses
    """
    def __init__(self):
        """Initializes a list of Expense Instances
        self.expense = expense

        Attributes:
            expense(list): a list to store Expense objects
        """
        # expenses list
        self.expenses:List  = []
        
        self.connection = psycopg.connect(
            host=os.environ.get('host'),
            port=os.environ.get('port'),
            dbname=os.environ.get('dbname'),
            user=os.environ.get('user'),
            password=os.environ.get('password')
        )

        # creates a cursor for execution of sql queries
        self.cur = self.connection.cursor()
    
    
    def add_expense(self, title:str, amount:float):
        """Adds an Expense instance to the database
        """
        expense = Expense(title, amount)
        self.expenses.append(expense)
        
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS exams.expense (
                id UUID,
                title VARCHAR(255),
                amount FLOAT,
                created_at TIMESTAMP,
                updated_at TIMESTAMP);
            """
            )
        
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
               FROM exams.expense
            """
        )
        
        # checks if an id inst in the database
        result = id_s.fetchall()
        if expense_id not in result:
            print(f"{expense_id} Not In Database")
            
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
                'id': str(expense[0]),                # Convert UUID to string
                'title': expense[1],
                'amount': expense[2],
                'created_at': expense[3].isoformat(),  # Format datetime
                'updated_at': expense[4].isoformat(),  # Format datetime
            }
            print(f_expense)
    
        # check if record exist on database
        id_s = self.cur.execute(
            """SELECT id
               FROM exams.expense
            """
        )
        
        ID = id_s.fetchall()
        if expense_id not in ID:
            print(f"{expense_id} Not In Database")
        
        self.connection.commit()
    
    
    def get_expense_by_title(self, expense_title:str) -> List[tuple]:
        """Retrieves expenses by title
        """
        
        # actual query
        records = self.cur.execute(
        """
        SELECT *
        FROM exams.expense
        WHERE exams.expense.title = %s
        """,
        expense_title
        )
        
        # check if record does not exist
        title = self.cur.execute(
            """SELECT title
               FROM exams.expense
            """
        )
        
        titles = title.fetchall()
        if expense_title not in titles:
            print(f"{expense_title} Not In Database")
        
        results = records.fetchall()
        return [expense for expense in results]
    
        self.connection.commit()


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
        
        self.connection.commit()
        
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
            self.expenses.append(expense)
    
    #self.cur.close()
    #self.connection.close()