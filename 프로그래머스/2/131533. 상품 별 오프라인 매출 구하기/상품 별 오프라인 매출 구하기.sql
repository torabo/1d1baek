SELECT pduct.PRODUCT_CODE
     , SUM(pduct.PRICE * sale.SALES_AMOUNT) as SALES
FROM OFFLINE_SALE sale
    INNER JOIN PRODUCT pduct ON sale.PRODUCT_ID = pduct.PRODUCT_ID
GROUP BY pduct.PRODUCT_CODE
ORDER BY SALES DESC , PRODUCT_CODE ASC