-- 코드를 입력하세요
SELECT 
CONCAT('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) as FILE_PATH
from
used_goods_file where board_id = 
( 
    select board_id from used_goods_board where 
  views = (select max(views) from used_goods_board)
)
order by  file_id desc