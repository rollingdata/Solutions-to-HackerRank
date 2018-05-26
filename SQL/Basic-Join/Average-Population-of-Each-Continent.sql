SELECT
    B.CONTINENT, FLOOR(AVG(A.POPULATION))
FROM
    CITY AS A
LEFT JOIN
    COUNTRY AS B ON B.CODE = A.COUNTRYCODE
WHERE
    B.CONTINENT IS NOT NULL
GROUP BY
    B.CONTINENT


/* Another solution */
SELECT
    Country.Continent, FLOOR(AVG(City.Population))
FROM
    Country, City
WHERE
    Country.Code = City.CountryCode
GROUP BY
    Country.Continent 
