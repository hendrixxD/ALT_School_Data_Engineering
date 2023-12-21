"""
Samples ExpensDB class methods
"""
import os
import random
import psycopg
from faker import Faker
from dotenv import load_dotenv
from expense import Expense
from expenseDB import ExpenseDB

# initialize faker object
fake = Faker()
# load environment variables
load_dotenv()

connection = psycopg.connect(
    host=os.environ.get('host'),
    port=os.environ.get('port'),
    dbname=os.environ.get('dbname'),
    user=os.environ.get('user'),
    password=os.environ.get('password')
    )

# creates a cursor for execution of sql queries
cur = connection.cursor()


def generate_fake_expense():
    """
    Generates fake expense data
    """
    title = fake.company()                 # Generate a fake word for the title
    amount = random.uniform(20000, 1000_000)   # Generate a random amount between 10 and 1000

    return title, amount


def main():
    
    exp_db = ExpenseDB()
    # exp_db.add_expense(title="Data Engineering", amount=200_000)
    
    #title = ["groceries", "school fees", "travel expenses", "house hold"]
    #amount = [340.00, 320.00, 29.000, 5.0000]

    #for title, amount in zip(title, amount):
    #    exp1 = exp_db.add_expense(title=title, amount=amount)
    #    print(exp1)
    
    """
    Generate fake expenses for demonstration
    """


    # Sample returning a dict for each expense
    try:
        cur.execute(
            """
            SELECT *
            FROM exams.expense
            LIMIT 1
            """
            )

        expenses = cur.fetchall()
        cur.connection.close()

        for expense in expenses:
            result = exp_db.to_dict()
        print(result)
            
    except Exception as e:
        print(f"{e}")

    
    
if __name__=='__main__':
    main()