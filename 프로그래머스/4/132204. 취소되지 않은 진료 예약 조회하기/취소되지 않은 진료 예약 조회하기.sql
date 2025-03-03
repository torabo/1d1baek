SELECT app.APNT_NO
        , p.PT_NAME
        , p.PT_NO
        , app.MCDP_CD
        , d.DR_NAME
        , app.APNT_YMD
FROM APPOINTMENT app
    INNER JOIN PATIENT as p ON p.PT_NO = app.PT_NO
    INNER JOIN DOCTOR as d ON d.DR_ID = app.MDDR_ID
WHERE APNT_YMD BETWEEN '2022-04-13 00:00:00' AND '2022-04-13 23:59:59'
AND APNT_CNCL_YN = 'N'
AND app.MCDP_CD = 'CS'
ORDER BY APNT_YMD ASC