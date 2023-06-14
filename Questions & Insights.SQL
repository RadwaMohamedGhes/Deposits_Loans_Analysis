-- QUEST 1: 
-- average of the average yearly balance per job
SELECT job, AVG(balance) avg_balance
FROM term_deposit
GROUP BY job
ORDER BY avg_balance DESC;
------------------------------------------------------------------------------------------------------------------------------

-- QUEST 2:
-- percentage rate of clients who subscribed according to their education level 
SELECT t.education, t.subscribed, COUNT(*) AS count, 
    ROUND(COUNT(*)*100/(SELECT COUNT(*) FROM term_deposit WHERE education = t.education), 2) AS percentage
FROM term_deposit t
WHERE subscribed = 'yes'
GROUP BY t.education, t.subscribed;
------------------------------------------------------------------------------------------------------------------------------

-- QUEST 3:
-- Number of subscribed clients according to having a personal loan or not
SELECT loan, Count(subscribed) as subscribed_count
FROM term_deposit
WHERE subscribed = 'yes'
GROUP BY loan;
------------------------------------------------------------------------------------------------------------------------------

-- QUEST 4:
-- average contact duration of clients who subscribed or not subscribed 
SELECT  subscribed, AVG(duration)
FROM term_deposit
GROUP BY subscribed;
---------------------------------------------------------------------------------


----------------------- ## Data Warehouse Analysis -------------------------
-- QUESTION 1: What is the cancellation rate of our term deposits?

WITH deposit_cancelled AS 
(
SELECT DISTINCT cancelled, COUNT(*) OVER(PARTITION BY cancelled) / COUNT(*) OVER() cancellation_rate
FROM transactions_fact t
JOIN services_dim s
ON t.service_id = s.service_id
WHERE transaction_type = 'Deposit' 
)
SELECT cancellation_rate
FROM deposit_cancelled
WHERE cancelled = 1;
----------------------------------------------------------------------------------------------------------------------------
-- QUESTION 2: What are the cancellation rates of each term deposit?

WITH deposit_cancelled AS 
(
SELECT DISTINCT cancelled, category, COUNT(*) OVER(PARTITION BY cancelled, category) / COUNT(*) OVER(PARTITION BY category) cancellation_rate
FROM transactions_fact t
JOIN services_dim s
ON t.service_id = s.service_id
WHERE transaction_type = 'Deposit' 
)
SELECT category, cancellation_rate
FROM deposit_cancelled
WHERE cancelled = 1;
----------------------------------------------------------------------------------------------------------------------------
-- QUESTION 3: What is the channel of communication that is most common?

SELECT channel_, COUNT(*) most_common_channel
FROM customer_services_fact
GROUP BY channel_
ORDER BY most_common_channel DESC;
----------------------------------------------------------------------------------------------------------------------------
-- QUESTION 4: What is the amount of profit we get from each customer?

SELECT fname||' '||lname client_name, SUM((INTEREST_RATE*AMOUNT)*
  (CASE 
    WHEN TRANSACTION_TYPE = 'Deposit' AND cancelled = 0 THEN -1 
    WHEN TRANSACTION_TYPE = 'Loan' AND approved = 1 AND cancelled = 0 THEN 1
    ELSE 0
  END)
   - NVL(EXPENSES,0)) AS profit 
FROM customer_dim c
JOIN transactions_fact t
ON c.customer_id = t.customer_id
JOIN services_dim s
ON t.service_id = s.service_id
GROUP BY fname||' '||lname
ORDER BY profit DESC;
----------------------------------------------------------------------------------------------------------------------------
-- QUESTION 5: What is the average subscribed clients per job?

SELECT job_, Avg(subscribed) subscribed_rate
FROM marketing_campaign_fact m
JOIN customer_dim c
ON m.customer_id = c.customer_id
GROUP BY job_
ORDER BY subscribed_rate DESC;
----------------------------------------------------------------------------------------------------------------------------
-- QUESTION 6: What is the total profit?

SELECT SUM((INTEREST_RATE*AMOUNT)*
  (CASE 
    WHEN TRANSACTION_TYPE = 'Deposit' AND cancelled = 0 THEN -1 
    WHEN TRANSACTION_TYPE = 'Loan' AND approved = 1 AND cancelled = 0 THEN 1
    ELSE 0
  END)
   - NVL(EXPENSES,0)) AS profit  
FROM transactions_fact t
JOIN services_dim s
ON t.service_id = s.service_id;
----------------------------------------------------------------------------------------------------------------------------
-- QUESTION 7: What is the Net amount of money we have ?

SELECT total - LEAD (total) OVER (ORDER BY total DESC) AS net
  FROM (  SELECT SUM (amount) total, transaction_type
            FROM services_dim S JOIN Transactions_Fact T USING (service_id)
           WHERE approved = 1 OR transaction_type = 'Deposit'
        GROUP BY transaction_type);
----------------------------------------------------------------------------------------------------------------------------
-- QUESTION 8: What is the Most common services?  
  SELECT transaction_type, category, COUNT (*) AS frequency
    FROM services_dim JOIN Transactions_Fact USING (Service_ID)
GROUP BY transaction_type, category
ORDER BY frequency DESC, transaction_type;
----------------------------------------------------------------------------------------------------------------------------
--QUESTION 9: Which customers respond to our campaigns the most (Age/Gender/Education/and so on).

---gender
  SELECT gender, AVG (subscribed) subscribtion_rate
    FROM    Customer_Dim c
         JOIN
            Marketing_Campaign_Fact m
         ON c.customer_id = m.customer_id
GROUP BY gender
ORDER BY subscribtion_rate DESC;

---education
  SELECT c.education, AVG (SUBSCRIBED) subscribtion_rate
    FROM    Customer_Dim c
         JOIN
            Marketing_Campaign_Fact m
         ON c.customer_id = m.customer_id
GROUP BY c.education
ORDER BY subscribtion_rate DESC;

---job
  SELECT c.job_, AVG (SUBSCRIBED) subscribtion_rate
    FROM    Customer_Dim c
         JOIN
            Marketing_Campaign_Fact m
         ON c.customer_id = m.customer_id
GROUP BY c.job_
ORDER BY subscribtion_rate DESC;


----age
-- avg age of subscribed customers
  SELECT SUBSCRIBED, AVG (age)
    FROM    Customer_Dim c
         JOIN
            Marketing_Campaign_Fact m
         ON c.customer_id = m.customer_id
GROUP BY SUBSCRIBED;

---Marital
  SELECT c.Marital, AVG (SUBSCRIBED) subscribtion_rate
    FROM    Customer_Dim c
         JOIN
            Marketing_Campaign_Fact m
         ON c.customer_id = m.customer_id
GROUP BY c.Marital
ORDER BY subscribtion_rate DESC;

--country
  SELECT c.country, AVG (SUBSCRIBED) subscribtion_rate
    FROM    Customer_Dim c
         JOIN
            Marketing_Campaign_Fact m
         ON c.customer_id = m.customer_id
GROUP BY c.country
ORDER BY subscribtion_rate DESC;

---Hosing loan
  SELECT c.Housing, AVG (SUBSCRIBED) subscribtion_rate
    FROM    Customer_Dim c
         JOIN
            Marketing_Campaign_Fact m
         ON c.customer_id = m.customer_id
GROUP BY c.Housing
ORDER BY subscribtion_rate DESC;

-- pesonal loan
  SELECT c.loan, AVG (SUBSCRIBED) subscribtion_rate
    FROM    Customer_Dim c
         JOIN
            Marketing_Campaign_Fact m
         ON c.customer_id = m.customer_id
GROUP BY c.loan
ORDER BY subscribtion_rate DESC;
----------------------------------------------------------------------------------------------------------------------------
-- QUESTION 10: What deposit types attract the most clients. 
---- NOTE THE SAME CATEGORRY HAVE DIFFERENT SERVICE ID BECAUSE EACH CATEGORY CAN CHANGE EVERY YEAR WITH RESPECT INTEREST RATE

-- Count of transactions
  SELECT CATEGORY, COUNT (*) AS count_
    FROM Services_Dim s JOIN Transactions_fact f ON S.SERVICE_ID = F.SERVICE_ID
   WHERE transaction_type = 'Deposit'
GROUP BY CATEGORY
ORDER BY count_ DESC;

---CANCELLATION RETE
SELECT AVG (CANCELLED) * 100 AS CANCELLATION_RATE
  FROM Services_Dim s JOIN Transactions_fact f ON S.SERVICE_ID = F.SERVICE_ID
 WHERE transaction_type = 'Deposit';

