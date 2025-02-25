-- 코드를 입력하세요
SELECT ins.ANIMAL_ID  
     , ins.ANIMAL_TYPE
     , ins.NAME
FROM ANIMAL_INS as ins
    INNER JOIN ANIMAL_OUTS as outs ON ins.ANIMAL_ID = outs.ANIMAL_ID
WHERE ins.SEX_UPON_INTAKE LIKE '%Intact%'
AND (outs.SEX_UPON_OUTCOME LIKE '%Spayed%'
OR outs.SEX_UPON_OUTCOME LIKE '%Neutered%'
)