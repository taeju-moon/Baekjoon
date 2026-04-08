-- 코드를 작성해주세요
select V.ID, K.FISH_NAME, K.LENGTH
from
fish_info V
inner join 
( select 
A.fish_type, B.FISH_NAME, max(A.LENGTH) as LENGTH
from 
fish_info A inner join fish_name_info B on A.fish_type = B.fish_type
group by A.fish_type, B.fish_name ) as K
on V.fish_type = K.fish_type
where V.length = K.length