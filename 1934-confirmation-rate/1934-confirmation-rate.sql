# Write your MySQL query statement below
# 확인된 메세지의 비율 구하는 문제
# cte에서 signup, confirmations 테이블을 left join한다
# cte 밖에서 sum(case when)을 활용해서 confirmed인 경우만 계산하고, sum(count)로 나눈다.
# cte밖에서 coalesce를 활용해서 confirmation_rate를 구한다.

with cte as (
    select s.user_id, s.time_stamp, action
    from signups as s
    left join confirmations as c
    on s.user_id = c.user_id
)

select user_id, 
       round(sum(case when action = 'confirmed' then 1 else 0 end)/count(user_id),2) as confirmation_rate
from cte
group by user_id
order by user_id 