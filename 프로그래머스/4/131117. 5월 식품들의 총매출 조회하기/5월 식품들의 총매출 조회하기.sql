SELECT A.PRODUCT_ID, B.PRODUCT_NAME, SUM(A.AMOUNT * B.PRICE) AS TOTAL_SALES
FROM FOOD_ORDER AS A
JOIN FOOD_PRODUCT AS B
ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE DATE_FORMAT(A.PRODUCE_DATE, '%Y%m') = '202205'
GROUP BY PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID