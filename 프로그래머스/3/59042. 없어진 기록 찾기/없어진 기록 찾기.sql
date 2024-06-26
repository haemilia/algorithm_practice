WITH I AS (
    SELECT ANIMAL_ID
    FROM ANIMAL_INS
)

SELECT O.ANIMAL_ID, NAME
FROM ANIMAL_OUTS O LEFT JOIN I ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID
;