SELECT book.CATEGORY
     , SUM(sales.SALES) AS TOTAL_SALES
FROM BOOK book
    INNER JOIN BOOK_SALES sales ON book.BOOK_ID = sales.BOOK_ID
WHERE sales.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY book.CATEGORY
ORDER BY CATEGORY ASC