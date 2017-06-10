

-- can replace avg into other aggregation funtions
SELECT round(avg(t1.LAT_N), 4) as median_val FROM (
SELECT @rownum:=@rownum+1 as `row_number`, s.LAT_N
  FROM STATION s,  (SELECT @rownum:=0) r
  WHERE 1
  -- put some where clause here
  ORDER BY s.LAT_N
) as t1,
(
  SELECT count(*) as total_rows
  FROM STATION s
  WHERE 1
  -- put same where clause here
) as t2
WHERE 1
AND t1.row_number in ( floor((total_rows+1)/2), floor((total_rows+2)/2) );


-- only works with table with odd row number
select round(S.LAT_N, 4) median from station S 
where (select count(Lat_N) from station where Lat_N < S.LAT_N ) =
      (select count(Lat_N) from station where Lat_N > S.LAT_N)
