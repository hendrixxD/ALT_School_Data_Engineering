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
GROUP BY
	txn_year, txn_type;
ORDER BY
	txn_year, txn_type;