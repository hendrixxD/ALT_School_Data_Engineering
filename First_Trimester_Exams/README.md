# Fall Semester Data Engineering Exams

## Synopsis
 The achieving goal of this project is to put to test and validate the knowledge OOP which we have ingested through out the the semester by implementing two classes that models and manages financial expenses.

## Classes

 ### Expense Class:
  This class represents an individual financial expense.
  
  Attributes:
   1. id: A unique identifier generated as a UUID string.
   2. title: A string representing the title of the expense.
   3. amount: A float representing the amount of the expense.
   4. created_at: A timestamp indicating when the expense was created (UTC).
   5. updated_at: A timestamp indicating the last time the expense was updated (UTC).
    
  Methods:
   1. __init__: Initializes the attributes.
   2. update: Allows updating the title and/or amount, updating the updated_at timestamp.
   3. to_dict: Returns a dictionary representation of the expense.
 
 
 ### ExpenseDB class
  Manages a collection of Expense objects.
  
  Attributes:
   1. expenses: A list storing Expense instances.
  
  Methods:
   1. __init__: Initializes the list.
   2. add_expense: Adds an expense.
   3. remove_expense: Removes an expense.
   4. get_expense_by_id: Retrieves an expense by ID.
   5. get_expense_by_title: Retrieves expenses by title.
   6. to_dict: Returns a list of dictionaries representing expenses.

## How To Clone

## How To Run




*The assignment will test your proficiency in defining classes, utilizing class attributes and methods,and handling time-related functionalities.*
