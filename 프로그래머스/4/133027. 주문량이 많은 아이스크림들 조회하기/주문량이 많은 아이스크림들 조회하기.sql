-- 코드를 입력하세요
select flavor from 
(
select 
flavor, sum(total_order) as total from
((select * from first_half) union all (select * from july)) as A group by flavor
    ) as K
order by K.total desc
limit 3
