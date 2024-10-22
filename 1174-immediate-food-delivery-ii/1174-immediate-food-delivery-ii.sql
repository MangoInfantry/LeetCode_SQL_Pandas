# Write your MySQL query statement below
# 어떤 주문이 모든 첫 주문들 중에서 immediate 판정을 받는 주문일 확률을 구하라 
# 먼저 첫 주문을 구한다. (dense_rank를 써서 1인 것들만 출력)
# 첫 주문들 중에 case when을 써서 order_date와 customer_pref가 같은 것들을 고르고 전체 주문 비율로 나눈다.

with cte as (
    select delivery_id,
        customer_id,
        order_date,
        customer_pref_delivery_date,
        dense_rank() over (partition by customer_id order by order_date) as rnk
    from delivery
)
select 100 * round(count(case when order_date = customer_pref_delivery_date then 1 end)/count(delivery_id),4) as immediate_percentage
from cte 
where rnk = 1