
-- Who are the top 3 members with the most bitcoin quantity? Your result should return
-- exactly two columns - first_name, total_quantity

SELECT
	first_name,
	SUM(quantity) total_quantity
FROM
	raw.members
JOIN
	raw.transactions ON members.member_id = transactions.member_id
WHERE
	ticker = 'BTC'
GROUP BY
	first_name
ORDER BY
	total_quantity desc
LIMIT 3;