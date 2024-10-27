# Write your MySQL query statement below
# 버스 무게 제한이 1000kg 이상
# 체중 제한을 초과하지 않고 버스에 탈 수 있는 마지막 사람의 name을 찾는 솔루션
# cte에서 sum이 있는 window function을 적용한다. 
# cte문 밖에서 누적합이 1000이 이하인 사람만 필터링 하고 limit 1을 적용한다.

with cte as (
    select person_name, sum(weight) over (order by turn asc) as cumsum
    from queue
)

select person_name
from cte
where cumsum<=1000
order by cumsum desc
limit 1
