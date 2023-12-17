#!/usr/bin/env python3
"""
a main script to test Expense class
"""
from expense import Expense

if __name__=='__main__':
    title = ["groceries", "school fees", "travel expenses", "house hols"]
    amount = [340.00, 320.00, 29.000, 5.0000]

    for title, amount in zip(title, amount):
        exp = Expense(title=title, amount=amount)
        
        print(exp.to_dict())


    

