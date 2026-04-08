-- 코드를 입력하세요
SELECT A.TITLE, A.BOARD_ID, B.REPLY_ID, B.WRITER_ID, B.CONTENTS, 
DATE_FORMAT(B.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from 
used_goods_board A inner join used_goods_reply B
on A.board_id = B.board_id
where
DATE_FORMAT(A.created_date, '%Y-%m') = '2022-10'
order by B.created_date asc, A.title asc