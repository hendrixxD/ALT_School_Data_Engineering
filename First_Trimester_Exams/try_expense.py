#!/usr/bin/env python3
"""
a main script to test Expense class
"""
import random
from faker import Faker
from expense import Expense

# Create a Faker instance
fake = Faker()

def generate_fake_expense():
    """
    Generate fake expense data using Faker.
    """
    title = fake.word()                 # Generate a fake word for the title
    amount = random.uniform(20000, 1000_000)   # Generate a random amount between 10 and 1000

    return title, amount


if __name__=='__main__':
    
    for _ in range(30):  # Generate 5 fake expenses for demonstration
        title, amount = generate_fake_expense()
        exp = Expense(title=title, amount=f"{amount:.2f}")
        print(exp.to_dict())
        #print(f"Title: {title}, Amount: ${amount:.2f}")
    

    #for title, amount in zip(title, amount):
    #    exp = Expense(title=title, amount=amount)
    #    
    #    print(exp.to_dict())

    
    
    


    

