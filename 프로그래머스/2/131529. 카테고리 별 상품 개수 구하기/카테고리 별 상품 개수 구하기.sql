SELECT   LEFT(PRODUCT_CODE,2) AS CATEGORY
        , COUNT(DISTINCT PRODUCT_ID) AS 'PRODUCTS'
FROM PRODUCT
GROUP BY CATEGORY