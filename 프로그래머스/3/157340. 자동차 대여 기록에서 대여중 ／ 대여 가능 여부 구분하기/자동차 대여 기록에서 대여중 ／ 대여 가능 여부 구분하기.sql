-- 코드를 입력하세요
SELECT D.CAR_ID, 
(case
 when exists(select * from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where 
     DATE_FORMAt(start_date, '%Y-%m-%d') <= '2022-10-16' and  '2022-10-16'<= DATE_FORMAt(end_date, '%Y-%m-%d')
       and car_id = D.car_id
 )then '대여중'
 else '대여 가능'
 end
) as AVAILABILITY
from (select distinct car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY) as D
order by D.car_id desc