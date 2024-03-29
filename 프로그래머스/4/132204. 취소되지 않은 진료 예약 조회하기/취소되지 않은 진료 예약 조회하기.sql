SELECT A.APNT_NO, C.PT_NAME, C.PT_NO, A.MCDP_CD, B.DR_NAME, A.APNT_YMD
FROM APPOINTMENT AS A
JOIN DOCTOR AS B
ON A.MDDR_ID = B.DR_ID
JOIN PATIENT AS C
ON A.PT_NO = C.PT_NO
WHERE A.MCDP_CD = 'CS' AND DATE_FORMAT(A.APNT_YMD, '%Y%m%d') = '20220413' AND (A.APNT_CNCL_YN = 'N' OR  A.APNT_CNCL_YN IS NULL)
ORDER BY APNT_YMD