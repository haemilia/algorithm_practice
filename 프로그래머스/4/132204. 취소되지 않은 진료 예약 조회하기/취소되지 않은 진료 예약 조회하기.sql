WITH P AS (SELECT PT_NO, PT_NAME 
		  FROM PATIENT),
D AS (SELECT DR_ID, DR_NAME
	 FROM DOCTOR)
SELECT A.APNT_NO, P.PT_NAME, A.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM APPOINTMENT A JOIN P ON A.PT_NO = P.PT_NO
JOIN D ON A.MDDR_ID = D.DR_ID
WHERE DATE(APNT_YMD) = "2022-04-13"
AND MCDP_CD = "CS"
AND APNT_CNCL_YN = "N"
ORDER BY APNT_YMD