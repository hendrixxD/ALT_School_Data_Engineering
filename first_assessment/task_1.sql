
-- CREATE a user `cryptoverse_admin` with CREATEDB and CREATEROLE attributes

-- CREATE USER cryptoverse_admin WITH CREATEDB CREATEROLE ENCRYPTED PASSWORD 'admin';
-- CREATE DATABASE metaverse;
-- SET role cryptoverse_admin;

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