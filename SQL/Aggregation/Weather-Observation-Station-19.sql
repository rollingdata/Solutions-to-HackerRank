SELECT ROUND(SQRT(POW(max(LAT_N) - min(LAT_N), 2) + POW(max(LONG_W) - min(LONG_W), 2)), 4)
FROM STATION
