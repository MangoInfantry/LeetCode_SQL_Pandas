# Write your MySQL query statement below
# 플레이어 별로 미니멈 데이트
with cte as (
    select player_id, 
           min(event_date) as event_date1  
    from activity
    group by player_id
)

select round((sum(case when date_add(event_date1, interval 1 day) = event_date then 1 else 0 end))/(count(distinct c.player_id)),2) as fraction
from cte as c
join activity as a
on c.player_id = a.player_id