-- 코드를 입력하세요
select 
AUTHOR_ID,
AUTHOR_NAME,
CATEGORY,
SUM(TOTAL_SALES)
from 
( SELECT 
AUTHOR_ID,
AUTHOR_NAME,
CATEGORY,
PRICE * SUM(SALES) as TOTAL_SALES
from
BOOK natural join AUTHOR natural join BOOK_SALES
where date_format(sales_date, '%Y-%m') = '2022-01'
group by author_id, category, price) as P
group by author_id, category
order by author_id asc, category desc
