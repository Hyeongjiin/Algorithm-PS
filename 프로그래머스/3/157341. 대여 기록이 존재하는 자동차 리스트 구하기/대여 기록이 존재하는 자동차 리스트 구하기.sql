SELECT DISTINCT A.CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS A
JOIN CAR_RENTAL_COMPANY_CAR AS B
ON A.CAR_ID = B.CAR_ID
WHERE B.CAR_TYPE = '세단' AND A.CAR_ID IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE >= '2022-10-01' AND START_DATE < '2022-11-01'
)
ORDER BY CAR_ID DESC