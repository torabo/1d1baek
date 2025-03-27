WITH cte as (SELECT ID
             , CASE WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 1 AND 3 THEN '1Q'
             WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 4 AND 6 THEN '2Q'
             WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 7 AND 9 THEN '3Q'
             WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 10 AND 12 THEN '4Q'
             END AS QUARTER
FROM ECOLI_DATA)

SELECT QUARTER
        , COUNT(ID) as ECOLI_COUNT
FROM cte 
GROUP BY QUARTER
ORDER BY QUARTER ASC