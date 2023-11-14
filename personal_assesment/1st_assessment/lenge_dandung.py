"""
author: devhendrixx@gmail.com
"""

question_one = """

SELECT
	txn_type,
	COUNT(quantity) AS transaction_count
FROM
	raw.transactions
WHERE
	ticker = 'BTC'
GROUP BY
	txn_type;

"""


question_two = """
SELECT 
	EXTRACT(YEAR FROM txn_date::DATE) AS txn_year,
	txn_type,
	COUNT(*) AS txn_count,
	SUM(quantity) AS total_quantity,
	AVG(quantity) AS average_quantity
FROM
	raw.transactions
WHERE
	ticker = 'BTC'
GROUP BY
	txn_year, txn_type
ORDER BY
	txn_year, txn_type;
"""


question_three = """
SELECT
	EXTRACT(MONTH FROM txn_date::DATE) AS calendar_month,
	SUM(CASE
			WHEN txn_type = 'BUY'
			THEN quantity ELSE 0
		END
	) AS buy_quantity,
	SUM(CASE
			WHEN txn_type = 'SELL'
			THEN quantity ELSE 0
		END
	) AS sell_quantity
FROM
	raw.transactions
WHERE
	ticker = 'ETH'
	AND EXTRACT(YEAR FROM txn_date::DATE) = 2020
GROUP BY
	calendar_month
ORDER BY
	calendar_month;
"""


question_four = """
SELECT
	first_name,
	SUM(quantity) AS total_quantity
FROM
	raw.members
JOIN
	raw.transactions ON members.member_id = transactions.member_id
WHERE
	ticker = 'BTC'
GROUP BY
	first_name
ORDER BY
	total_quantity DESC
LIMIT 3;
"""