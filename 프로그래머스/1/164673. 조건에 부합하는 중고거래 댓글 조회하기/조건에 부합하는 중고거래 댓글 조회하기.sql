SELECT bo.TITLE
        ,bo.BOARD_ID
        ,re.REPLY_ID
        ,re.WRITER_ID
        ,re.CONTENTS
        ,DATE_FORMAT(re.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
FROM USED_GOODS_BOARD bo
    INNER JOIN USED_GOODS_REPLY re ON re.BOARD_ID = bo.BOARD_ID 
WHERE bo.CREATED_DATE BETWEEN '2022-10-01 00:00:00' AND '2022-10-31 23:59:59'
ORDER BY CREATED_DATE ASC, bo.TITLE ASC