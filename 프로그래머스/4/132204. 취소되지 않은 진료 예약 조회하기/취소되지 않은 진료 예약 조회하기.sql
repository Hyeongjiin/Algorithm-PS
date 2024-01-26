-- 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회
-- 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시
-- APPOINTMENT - 예약 취소 여부 NULL 존재

SELECT A.APNT_NO, C.PT_NAME, A.PT_NO, A.MCDP_CD, B.DR_NAME, A.APNT_YMD
FROM APPOINTMENT AS A
JOIN DOCTOR AS B
ON A.MDDR_ID = B.DR_ID
JOIN PATIENT AS C
ON A.PT_NO = C.PT_NO
WHERE DATE_FORMAT(A.APNT_YMD, '%Y-%m-%d') = '2022-04-13' AND A.APNT_CNCL_YN = 'N'
ORDER BY A.APNT_YMD