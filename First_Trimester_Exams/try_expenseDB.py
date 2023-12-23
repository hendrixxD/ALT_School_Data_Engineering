"""
Sample ExpensDB class methods
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
    # Generate a fake word for the title
    title = fake.company()
    # Generate a random amount between 10 and 1000
    amount = random.uniform(20000, 1000_000)

    return title, amount


def main():
    
    DB = ExpenseDB()
    # exp_db.add_expense(title="Data Engineering", amount=200_000)
    
    #title = ["groceries", "school fees", "travel expenses", "house hold"]
    #amount = [340.00, 320.00, 29.000, 5.0000]

    #for title, amount in zip(title, amount):
    #    exp1 = exp_db.add_expense(title=title, amount=amount)
    #    print(exp1)

    
    # SAMPLES ADDING AN EXPENSE TO A DATABASE
    # try:
    #     for _ in range(400):
    #         title, amount = generate_fake_expense()
    #         exp = DB.add_expense(title=title, amount=f"{amount:.2f}")
    #     print(f"{_} Records added to database successfully")
    # except Exception as err:
    #     print(f"{err}")
    
    
    # SAMPLE THE REMOVAL OF N NUMBER OF EXPENSE BY ID FROM THE DATABASE
    # try:
    #     cur.execute(
    #         """
    #         SELECT exams.expense.id  AS id
    #         FROM exams.expense
    #         OFFSET 50
    #         """
    #     )
    
    #     expense_id = cur.fetchall()
    #     # cur.connection.close()    
    #     # print(expense_id)

    #     for exp_id in expense_id:
    #         # expense_id=exp
    #         DB.remove_expense(expense_id=exp_id)
    #         print(f"{str(exp_id)} removed successfully")
    # except Exception as e:
    #     print(f"{e}")
    
    
    # # Sample retrieving and expense by id
    # try:
    #     cur.execute(
    #         """
    #         SELECT id
    #         FROM exams.expense
    #         LIMIT 10;
    #         """
    #         )
    
    #     expense_by_id = cur.fetchall()
    #     cur.connection.close()

    #     for exp_id in expense_by_id:
    #         DB.get_expense_by_id(expense_id=exp_id)
            
    # except Exception as e:
    #     print(f"{e}")
    
    
    # Sample retrieving and expenses by title
    # try:
    #     cur.execute(
    #         """
    #         SELECT title
    #         FROM exams.expense
    #         LIMIT 5
    #         """
    #         )

    #     expenses_by_title = cur.fetchall()

    #     for exp_title in expenses_by_title:
    #         DB.get_expense_by_title(expense_title=exp_title)
            
    # except Exception as e:
    #     print(f"{e}")
    
    
    # Sample returning a dict for each expense
    try:
        result = DB.to_dict()
        print(result)
            
    except Exception as e:
        print(f"{e}")
    
if __name__=='__main__':
    main()