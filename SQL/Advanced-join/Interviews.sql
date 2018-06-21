SELECT con.contest_id, con.hacker_id, con.name, SUM(total_submissions),
    SUM(total_accepted_submissions), SUM(total_views), SUM(total_unique_views)
FROM Contests as con
JOIN Colleges as col on con.contest_id = col.contest_id
JOIN Challenges as cha on cha.college_id = col.college_id 
LEFT JOIN 
(SELECT challenge_id, sum(total_views) as total_views, sum(total_unique_views) as total_unique_views
from view_stats group by challenge_id) vs on cha.challenge_id = vs.challenge_id 
LEFT JOIN
(SELECT challenge_id, sum(total_submissions) as total_submissions, 
    sum(total_accepted_submissions) as total_accepted_submissions 
    from submission_stats 
    group by challenge_id) ss on cha.challenge_id = ss.challenge_id
GROUP BY con.contest_id, con.hacker_id, con.name
HAVING
    SUM(total_submissions) > 0 AND 
    SUM(total_accepted_submissions) > 0 AND 
    SUM(total_views) > 0 AND
    SUM(total_unique_views) > 0
ORDER BY con.contest_id