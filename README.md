# A single repository for Alt School Data Engineering

## Tinyuka Semester

 ### First Assignment
 In this assignment, we are tasked with answering a few business questions on the following csv files:
  - [members.csv](./first_assessment/members.csv)
  - [prices.csv](./first_assessment/prices.csv)
  - [transactions.csv](./first_assessment/transactions.csv)

 1. How many buy and sell transactions are there for Bitcoin? - your result should return two columns - `txn_type`,
 `transaction_count`
 2. For each year, calculate the following buy and sell metrics for bitcoin:
 - a. Total transaction count
 - b. Total quantity
 - c. Average quantity
 Kindly note that you are generating a single query to calculate these metrics and you should return exactly 5 columns: `txn_year`, `txn_type`, `txn_count`, `total_quantity`, `average_quantity`
 3. What was the monthly total quantity purchased and sold for Ethereum in 2020? Your
 query should return exactly three columns - `calendar_month`, `buy_qunatity`, `sell_quantity`
 4. Who are the top 3 members with the most bitcoin quantity? Your result should return
exactly two columns - `first_name`, `total_quantity`