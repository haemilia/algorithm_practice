WITH U AS (SELECT USER_ID, NICKNAME
FROM USED_GOODS_USER)

SELECT U.USER_ID, U.NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS B JOIN U ON U.USER_ID = B.WRITER_ID
WHERE STATUS = "DONE"
GROUP BY B.WRITER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES
;