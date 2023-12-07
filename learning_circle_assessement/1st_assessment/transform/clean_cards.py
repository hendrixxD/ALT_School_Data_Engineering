import os
import uuid
import pandas as pd

def wrangle(file_path):
    """
    This function takes a file path as an argument
    and perfomr transform operations
    """
    df = pd.read_csv(cards_path)
    
    # drop rows with missing values
    df = df.dropna()
    
    df = df.fillna(value=0)
    
    # cast float64 to int
    df["user_id"] = df[["user_id"]].astype('int64')
    
    #convert `event_id` to str
    df["event_id"] = df[["event_id"]].astype('str')
    
    # cast object to datetime object
    datetime_cols = ["created_at", "updated_at", "event_at"]
    df[datetime_cols] = df[datetime_cols].apply(pd.to_datetime)
    
    # Remove duplicate rows
    df = df.drop_duplicates()

    df.to_csv("tranform_cards.csv")
 

if __name__ == "__main__":
    cards_path = '/home/hendrixxdiddy/DEV/ALT_School_Data_Engineering/learning_circle_assessement/1st_assessment/cards.csv'
    users_path2 = '/home/hendrixxdiddy/DEV/ALT_School_Data_Engineering/learning_circle_assessement/1st_assessment/users.csv'
    
    print("Transformin cards data set...")
    wrangle(cards_path)
    print("Done, Data set transfromed successfully!!!")
    