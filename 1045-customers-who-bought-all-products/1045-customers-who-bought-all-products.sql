# Write your MySQL query statement below
# 제품 테이블에 있는 모든 제품을 구매한 고객을 찾아야 함
with cte as (
    select customer_id, product_key, lead(product_key,1) over (partition by customer_id)as product_key1
    from customer 
) 

select customer_id
from cte
where product_key1 is not null
order by customer_id