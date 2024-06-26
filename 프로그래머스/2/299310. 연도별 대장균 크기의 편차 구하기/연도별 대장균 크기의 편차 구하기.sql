SELECT A.YEAR, (B.MV - A.SIZE_OF_COLONY) AS YEAR_DEV, ID
FROM (SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, ID, SIZE_OF_COLONY
     FROM ECOLI_DATA) AS A JOIN
     (SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) AS MV
      FROM ECOLI_DATA
      GROUP BY YEAR) AS B ON A.YEAR = B.YEAR
ORDER BY A.YEAR, YEAR_DEV
;