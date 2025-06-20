SELECT SUM(C.SCORE) AS SCORE, C.EMP_NO, B.EMP_NAME, B.POSITION, B.EMAIL
FROM HR_DEPARTMENT A
RIGHT JOIN HR_EMPLOYEES B
ON A.DEPT_ID = B.DEPT_ID
LEFT JOIN HR_GRADE C
ON B.EMP_NO = C.EMP_NO
WHERE C.YEAR = 2022
GROUP BY B.EMP_NO
ORDER BY SCORE DESC
LIMIT 1