/* join salaries by different id col twice */


SELECT s.Name
FROM Friends as f
LEFT JOIN Students as s on f.ID = s.ID
LEFT JOIN Packages as p1 on f.ID = p1.ID
LEFT JOIN Packages as p2 on f.Friend_ID = p2.ID
WHERE p1.Salary < p2.Salary
ORDER BY p2.Salary
