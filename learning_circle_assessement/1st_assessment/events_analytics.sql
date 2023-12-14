
-- BASIC STATISTICS ON DEMOGRAPHICS(users.):
	
	-- What is the total count of users in the dataset?
	 --There are 1000 distinct users
select count(distinct(id)) 
from events.users u

   -- Can you provide a breakdown of users based on job titles?
	-- Atleast 3 different job titles appeard 6 times
select job, count(*) job_count
from events.users group by job order by job_count desc;
	
	-- at least 8 users got morethan 2 job titles
select name, count(job) as differennt_job_titles 
from events.users u
group by name order by differennt_job_titles desc;

 	--How many unique addresses are present in the dataset?
	 -- there are 1000 distinct addresses unique to every user
select distinct count(address) from events.users;



--EVENT-LEVEL DATA:
        --What is the total number of card events recorded?
		 -- There are 5,386  cards event 
select count(*) from events.trans_cards tc;
	   	
       --Can we identify the different types of events captured in the "type" column?
		 -- There are only cards eventc all through
select distinct "type" from events.trans_cards tc;
	  
        --Is there any missing or inconsistent data in the "event_id" column?
		 -- None, There are no missing or null columns. all consistent
SELECT event_id, COUNT(*) as count
FROM events.trans_cards
GROUP BY event_id
HAVING COUNT(*) > 1 OR event_id IS NULL;


--TIME_DAY ANALYSSIS
	 --What is the time range covered by the events in the dataset?
	  -- events were between 23:08:50 to 23:30:32 same day 2023
select                                
  COUNT(*) AS total_rows,            
  MIN(created_at) AS min_created_at,
  MAX(created_at) AS max_created_at
FROM events.trans_cards cards;
	
     --Are there specific patterns or trends in card events throughout the day?
	  -- Peak period for events was around 23:09 to 23:10 same day with 634 and 524 events respectively
select
  substr(created_at, 12,5) Hr,
  count(*) event_count
from
  events.trans_cards
group by substr(created_at, 12,5)
order by event_count desc;



-- USER INTERACTION:
	-- How many unique users are represented in the card events dataset?
	 -- There are 5,386 unique users represented in the events dataset
select distinct count(user_id) unique_user_id from events.trans_cards cards;
        
	-- Can we identify the users who have the highest and lowest engagement with card events?
	 -- user_id 429 had the highest card engaement. 100 users had the least engagment
select user_id, "name", count(*) engagement
from events.trans_cards tc
join events.users on tc.user_id = events.users.id 
group by user_id, "name"
order by engagement desc;

WITH UserEngagement AS (
  SELECT
  user_id, created_by_name, COUNT(*) as engagement_count
  FROM events.trans_cards
  GROUP BY user_id, created_by_name
)
SELECT
user_id, created_by_name, engagement_count,
RANK() OVER (ORDER BY engagement_count DESC) as engagement_rank
FROM UserEngagement
ORDER BY engagement_rank;

	--What are the distinct types of card-related events, and how frequently do they occur?
	 -- There are 5,386 distinct types of card-related events
select type, COUNT(distinct event_id) as event_count
FROM events.trans_cards
GROUP BY type
ORDER BY event_count DESC;

	--Are there any specific event types that stand out in terms of frequency or significance?
	 -- There is only a single type of event which is 'card'
select type,COUNT(*) as event_count
FROM events.trans_cards
GROUP BY type
ORDER BY event_count DESC
LIMIT 5;



-- COMBINED ANALYSIS:
	--How many users from the "users.csv" dataset have associated card events in the "cards.csv" dataset?
	 -- 911 users from users have associated cards
SELECT COUNT(DISTINCT u.id) as users_with_card_events
FROM events.users u
JOIN events.trans_cards c ON u.id = c.user_id;


