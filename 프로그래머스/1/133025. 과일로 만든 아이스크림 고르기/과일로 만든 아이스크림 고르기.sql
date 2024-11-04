-- 코드를 입력하세요.
SELECT f.FLAVOR FROM FIRST_HALF f
JOIN ICECREAM_INFO as i ON f.flavor = i.flavor
WHERE (f.total_order > 3000) and (i.INGREDIENT_TYPE = "fruit_based")
ORDER BY f.total_order DESC