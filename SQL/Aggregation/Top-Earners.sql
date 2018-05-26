SELECT salary * months AS earnings, COUNT(*)
FROM Employee
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1

SELECT salary*months as earnings, COUNT(*) FROM employee
WHERE salary*months = (SELECT MAX(salary*months) FROM employee)
GROUP BY earnings
