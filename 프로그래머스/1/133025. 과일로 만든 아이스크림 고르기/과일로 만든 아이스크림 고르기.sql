SELECT half.FLAVOR
FROM FIRST_HALF as half
    INNER JOIN ICECREAM_INFO as info ON half.FLAVOR = info.FLAVOR
WHERE half.TOTAL_ORDER > 3000 AND info.INGREDIENT_TYPE = 'fruit_based'