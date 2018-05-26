SELECT
    sum(A.POPULATION)
FROM
    CITY AS A
LEFT JOIN
    COUNTRY AS B
ON
    A.CountryCode = B.Code
WHERE
    B.CONTINENT = 'Asia'
