

SELECT CONCAT(Name, '(', SUBSTRING(Occupation, 1, 1), ')') AS new_name
FROM OCCUPATIONS
ORDER BY new_name;

SELECT 'There are total', COUNT(Name), CONCAT(LOWER(Occupation), 's.')
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(Name), Occupation ASC;
