# Write your MySQL query statement below
# 판매된 모든 제품의 첫 해의 제품 id, 연도, 수량, 가격을 출력

with cte as (
    select s.product_id,
       year,
       quantity,
       price,
       rank () over (partition by s.product_id order by year asc) as rnk
    from sales as s
    join product as p
    on s.product_id = p.product_id 
)

select product_id, year as first_year, quantity, price 
from cte
where rnk = 1
