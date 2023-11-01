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