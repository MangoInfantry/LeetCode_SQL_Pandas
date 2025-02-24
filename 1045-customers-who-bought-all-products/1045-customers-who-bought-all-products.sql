# Write your MySQL query statement below
# 제품 테이블의 모든 제품을 구매한 고객 테이블의 고객 ID를 보고하는 솔루션을 작성합니다.
# 결과 테이블을 임의의 순서로 반환합니다.
# 결과 형식은 다음 예제와 같습니다.

# cte에서 group by를 이용해 customer_id 별 product key의 갯수를 세준다. 
# cte2에서 product 테이블에서 product_key를 이용해 count를 세줘서 cte2를 만든다. 
# 조인을 이용하여 cte2에 있는 cnt와 cte에 있는 cnt와 같을 경우의 customer_id를 가져온다.  
with cte as (
    select distinct customer_id, count(distinct product_key) as cnt
    from customer
    group by customer_id
), cte2 as (
    select count(distinct product_key) as cnt 
    from product
)

select customer_id
from cte
join cte2 
on cte.cnt = cte2.cnt

