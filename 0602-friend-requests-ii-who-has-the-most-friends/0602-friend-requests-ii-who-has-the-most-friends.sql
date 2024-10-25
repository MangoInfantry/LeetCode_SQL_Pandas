# Write your MySQL query statement below
# 가장 많은 친구를 가진 사람과 가장 많은 친구 수를 찾는 솔루션을 작성합니다.
# cte1에 group by으로 count(requested_id)를 센다 
# cte2에 group by으로 count(accepter_id)를 센다 
# count(requested_id)열과 count(accepter_id)열을 cte에서 더한 다음에 cte밖에서 최대치를 구한다

with cte1 as (
    select requester_id as id,
            count(requester_id) as cnt
    from requestaccepted
    group by requester_id
), cte2 as(
    select accepter_id as id,
           count(accepter_id) as cnt
      from requestaccepted
      group by accepter_id
), cte3 as(
    select *
      from cte1
    union all
    select *
      from cte2
), cte4 as (
    select id, sum(cnt) as num
    from cte3
    group by id
)

select id, num
from cte4
order by num desc
limit 1