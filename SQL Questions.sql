QUEST 1: 
-- average of the average yearly balance per job
SELECT job, AVG(balance) avg_balance
FROM term_deposit
GROUP BY job
ORDER BY avg_balance DESC;
------------------------------------------------------------------------------------------------------------------------------

QUEST 2:
-- percentage rate of clients who subscribed according to their education level 
SELECT t.education, t.subscribed, COUNT(*) AS count, 
    ROUND(COUNT(*)*100/(SELECT COUNT(*) FROM term_deposit WHERE education = t.education), 2) AS percentage
FROM term_deposit t
WHERE subscribed = 'yes'
GROUP BY t.education, t.subscribed;
------------------------------------------------------------------------------------------------------------------------------

QUEST 3:
-- Number of subscribed clients according to having a personal loan or not
SELECT loan, Count(subscribed) as subscribed_count
FROM term_deposit
WHERE subscribed = 'yes'
GROUP BY loan;
------------------------------------------------------------------------------------------------------------------------------

QUEST 4:
-- average contact duration of clients who subscribed or not subscribed 
SELECT  subscribed, AVG(duration)
FROM term_deposit
GROUP BY subscribed;