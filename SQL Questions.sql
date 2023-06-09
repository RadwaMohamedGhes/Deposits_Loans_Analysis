QUEST 1:
-- average of the average yearly balance per job
SELECT job, AVG(balance) avg_balance
FROM term_deposit
GROUP BY job
ORDER BY avg_balance DESC;
--------------------------------------------------------------------------------------------------------------------------------------------

QUEST 2:
SELECT t.education, t.subscribed, COUNT(*) AS count, -- number of clients who subscribed or not according to their education level 
-- percentage rate of clients who subscribed or not according to their education level 
    ROUND(COUNT(*)*100/(SELECT COUNT(*) FROM term_deposit), 2) AS percentage,
-- number of clients in each education level
    (SELECT COUNT(*) FROM term_deposit WHERE education = t.education) AS total_count,
-- percentage of clients in each education level 
    ROUND((SELECT COUNT(*) FROM term_deposit WHERE education = t.education)*100/(SELECT COUNT(*) FROM term_deposit), 2) AS total_percentage
FROM term_deposit t
GROUP BY t.education, t.subscribed
ORDER BY education;
--------------------------------------------------------------------------------------------------------------------------------------------

QUEST 3:
-- Number of subscribed clients according to having a personal loan or not
SELECT loan, Count(subscribed) as subscribed_count
FROM term_deposit
WHERE subscribed = 'yes'
GROUP BY loan;
--------------------------------------------------------------------------------------------------------------------------------------------

QUEST 4:
-- average contact duration of clients who subscribed or not subscribed 
SELECT  subscribed, AVG(duration)
FROM term_deposit
GROUP BY subscribed;