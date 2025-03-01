SELECT usr.USER_ID
        , usr.NICKNAME
        , CONCAT(usr.CITY,' ', usr.STREET_ADDRESS1, ' ',usr.STREET_ADDRESS2) as '전체주소'
        , CONCAT(SUBSTR(usr.TLNO,1,3) ,'-' , 
                 SUBSTR(usr.TLNO,4,4) , '-' ,
                 SUBSTR(usr.TLNO,8,4)) as '전화번호'
FROM USED_GOODS_BOARD as brd
    INNER JOIN USED_GOODS_USER as usr ON brd.WRITER_ID = usr.USER_ID
WHERE brd.WRITER_ID IN (SELECT DISTINCT WRITER_ID 
                        FROM USED_GOODS_BOARD 
                        GROUP BY WRITER_ID
                        HAVING COUNT(WRITER_ID) >=3)
GROUP BY usr.USER_ID
ORDER BY usr.USER_ID DESC