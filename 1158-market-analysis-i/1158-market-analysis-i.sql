# Write your MySQL query statement below
# 2019년에 주문한 주문 건수와 바이어 아이디를 가져오는 문제
# users 테이블과 orders 테이블을 묶음 (orders 테이블은 year(order_date)가 2019년이어야 함)
# item_id은 user와 order가 조인한 후 조인

with cte as (
    select user_id, join_date, item_id, order_date
    from users as u
    left join orders as o
    on u.user_id = o.buyer_id 
)

select user_id as buyer_id, 
       join_date,
       sum(case when left(order_date,4)='2019' then 1 else 0 end) as orders_in_2019
from cte
group by buyer_id