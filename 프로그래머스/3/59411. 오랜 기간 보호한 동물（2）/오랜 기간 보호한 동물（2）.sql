SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS AS A
JOIN ANIMAL_INS AS B
ON A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY DATEDIFF(A.DATETIME, B.DATETIME) DESC
LIMIT 2