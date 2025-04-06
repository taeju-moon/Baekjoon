-- 코드를 입력하세요
SELECT 
count(distinct(NAME))
from animal_ins
where NAME IS NOT NULL
