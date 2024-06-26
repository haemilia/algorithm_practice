WITH A AS (SELECT CAR_ID, 
    (CASE
        WHEN START_DATE <= "2022-10-16" AND END_DATE >= "2022-10-16"
            THEN TRUE
        ELSE FALSE
    END) AS "AVAILABLE"
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY)
SELECT CAR_ID, (IF(SUM(AVAILABLE) > 0, "대여중", "대여 가능")) AS "AVAILABILITY"
FROM A
GROUP BY CAR_ID
ORDER BY CAR_ID DESC
;