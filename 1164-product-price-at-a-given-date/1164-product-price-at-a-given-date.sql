# Write your MySQL query statement below
# 2019-08-16에 모든 제품의 가격을 구하는 솔루션을 작성합니다. 변경 전 모든 제품의 가격이 10이라고 가정합니다.
# cte에서 change_date가 8월 16일 이전에 있는 것을 구한다. 그리고 cte2에서 8월 16일 이후의 데이터를 구하해서 가져온다.
# cte2의 데이터의 경우 10달러로 교체해준 다음 union all을 이용하여 

with cte as (
    select product_id, new_price, change_date, dense_rank() over (partition by product_id order by change_date desc) as rk
    from products
    where change_date <= '2019-08-16'
), cte2 as (
    select product_id, new_price
    from cte
    where rk = 1

    union all

    select product_id, 10 as new_price
    from products
    where change_date > '2019-08-16'
), cte3 as (
    select distinct(product_id) as product_id, new_price as price, dense_rank() over (partition by product_id order by new_price desc) as rnk
    from cte2
    order by product_id asc
)

select product_id, price
from cte3
where rnk = 1