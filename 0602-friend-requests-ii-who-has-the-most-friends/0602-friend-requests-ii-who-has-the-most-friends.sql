# Write your MySQL query statement below
# 가장 많은 친구를 가진 사람과 가장 많은 친구 수를 찾는 솔루션을 작성합니다.
# cte1 테이블: requester_id의 개수를 센다
# cte2 테이블: accepter_id의 개수를 센다
# cte3 테이블: cte1과 cte2를 조인한다
# cte4 테이블: re_count와 ac_count를 더해서 num을 만든다
# cte밖: cte4에서 order by를 이용하여 num을 정렬한다음, limit 1만 출력한다. 

with cte1 as (
    select requester_id as id, count(requester_id) as counts
    from RequestAccepted
    group by requester_id
), cte2 as (
    select accepter_id as id, count(accepter_id) as counts
    from RequestAccepted
    group by accepter_id
), cte3 as (
    select cte1.id, counts
    from cte1
    union all 
    select cte2.id, counts
    from cte2
), cte4 as (
    select id, sum(counts) as num
    from cte3
    group by id
)

select id, num 
from cte4
order by num desc 
limit 1