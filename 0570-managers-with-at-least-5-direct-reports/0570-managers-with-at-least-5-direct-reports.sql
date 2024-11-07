# Write your MySQL query statement below
# cte에서 managerId의 개수를 센 쿼리를 반환한다.
# 일반 select문에서 cte안에 managerId의 카운트가 5개가 넘는 managerId를 가진 name을 반환하도록 한다.

with cte as (
    select managerId, count(managerId) as cnt
    from employee
    group by managerId
)

select name
from employee
where id in (select managerId
               from cte
              where cnt>=5)