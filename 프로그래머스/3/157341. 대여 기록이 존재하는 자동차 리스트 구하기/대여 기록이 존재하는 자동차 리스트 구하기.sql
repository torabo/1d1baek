SELECT DISTINCT car.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR car
    LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY hist ON car.CAR_ID = hist.CAR_ID
WHERE car.CAR_TYPE = '세단' 
    AND hist.START_DATE BETWEEN '2022-10-01' AND '2022-10-31' 
ORDER BY car.CAR_ID DESC