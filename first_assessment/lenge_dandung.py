"""
author: devhendrixx@gmail.com
"""

question_one = """
SELECT 
	EXTRACT(YEAR FROM txn_date::DATE) txn_year,
	txn_type,
	COUNT(*) txn_count,
	SUM(quantity) total_quantity,
	AVG(quantity) average_quantity
FROM
	raw.transactions
WHERE
	ticker = 'BTC'
GROUP BY txn_year, txn_type;
ORDER BY txn_year, txn_type;
"""


question_two = """
SELECT 
	EXTRACT(YEAR from txn_date::date) txn_year,
	txn_type,
	COUNT(*) txn_count,
	SUM(quantity) total_quantity,
	AVG(quantity) average_quantity
FROM
	raw.transactions
WHERE
	ticker = 'BTC'
GROUP BY
	txn_year, txn_type;
ORDER
	BY txn_year, txn_type;
"""


question_three = """
SELECT
	EXTRACT(
     	MONTH FROM market_date::DATE) calender_month,
	SUM(
     	CASE WHEN price >= open THEN REGEXP_REPLACE(volume, '[^0-9.]', '', 'g')::NUMERIC ELSE 0 END) buy_quantity,
	SUM(
     	CASE WHEN price < open THEN REGEXP_REPLACE(volume, '[^0-9.]', '', 'g')::NUMERIC ELSE 0 END) sell_quantity
FROM
	raw.prices
WHERE
	ticker = 'ETH'
	AND EXTRACT(
     	YEAR FROM market_date::DATE) = 2020
GROUP BY
	calender_month
ORDER By
   calender_month;
"""


question_four = """
SELECT
	first_name,
	SUM(quantity) total_quantity
FROM
	raw.members
JOIN
	raw.transactions on members.member_id = transactions.member_id
WHERE
	ticker = 'BTC'
GROUP BY
	first_name
ORDER BY
	total_quantity desc
LIMIT 3;
"""