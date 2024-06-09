SELECT YEAR(SALES_DATE) YEAR, MONTH(SALES_DATE) MONTH, COUNT(DISTINCT A.USER_ID) PURCHASED_USERS, ROUND(COUNT(DISTINCT A.USER_ID) / (SELECT COUNT(USER_ID) FROM USER_INFO WHERE YEAR(JOINED) = 2021), 1) PURCHASED_RATIO
FROM USER_INFO A JOIN ONLINE_SALE B ON A.USER_ID = B.USER_ID
WHERE YEAR(JOINED) = 2021
GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE)
ORDER BY YEAR, MONTH