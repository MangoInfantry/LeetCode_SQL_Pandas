# Write your MySQL query statement below
# 각 사용자가 이동한 거리를 보고하는 솔루션을 작성합니다.
# travelled_distance를 기준으로 내림차순으로 정렬된 결과 테이블을 반환하고, 두 명 이상의 사용자가 같은 거리를 이동한 경우 이름 순으로 오름차순으로 정렬

with cte as (
    select name,u.id, case when distance is null then 0 else distance end as distance
    from users as u
    left join rides as r
    on u.id = r.user_id
    order by distance desc
)

select distinct name, sum(distance) over (partition by id) as travelled_distance
from cte 
order by travelled_distance desc, name asc

