SELECT COUNT(ID) AS FISH_COUNT, CAST(MONTH(TIME) AS DECIMAL) AS MONTH
FROM FISH_INFO
GROUP BY MONTH
ORDER BY MONTH
;