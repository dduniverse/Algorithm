SELECT QUARTER, COUNT(ID) AS ECOLI_COUNT
FROM (
    SELECT
        *,
        CASE
            WHEN MONTH(DIFFERENTIATION_DATE) >= 10 THEN '4Q'
            WHEN MONTH(DIFFERENTIATION_DATE) >= 7 THEN '3Q'
            WHEN MONTH(DIFFERENTIATION_DATE) >= 4 THEN '2Q'
            ELSE '1Q'
        END AS QUARTER
    FROM ECOLI_DATA
) AS A
GROUP BY QUARTER
ORDER BY QUARTER ASC