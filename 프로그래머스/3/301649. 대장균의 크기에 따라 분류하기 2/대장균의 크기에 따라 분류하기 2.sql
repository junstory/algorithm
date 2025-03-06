-- 코드를 작성해주세요
SELECT  ID,
        CASE
        WHEN 1 -percent_rank() over(order by size_of_colony) <=0.25 
        THEN "CRITICAL"
        WHEN 1 -percent_rank() over(order by size_of_colony) <=0.5 
        THEN "HIGH"
        WHEN 1 -percent_rank() over(order by size_of_colony) <=0.75
        THEN "MEDIUM"
        ELSE "LOW"
        END COLONY_NAME
        FROM ECOLI_DATA
        ORDER BY ID