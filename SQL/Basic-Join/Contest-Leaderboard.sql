SELECT h.hacker_id, h.name, sum(s.m_score) 
FROM Hackers as h
INNER JOIN 
    (SELECT hacker_id, challenge_id, MAX(score) as m_score
    FROM Submissions
    GROUP BY hacker_id, challenge_id
    ORDER BY hacker_id) as s 
ON h.hacker_id = s.hacker_id
GROUP BY h.hacker_id, h.name
HAVING sum(s.m_score) <> 0
ORDER BY sum(s.m_score) DESC, h.hacker_id