# Write your MySQL query statement below
with cte as (select num,
             id,      
             lead(id,1) over (order by id) as id1,
             lead(id, 2) over (order by id) as id2,
             lead(num,1) over (order by id) as lead1,
             lead(num,2) over (order by id) as lead2
             from logs)

select distinct(num) as consecutivenums
from cte
where (num = lead1) and (num = lead2) and (id+1 = id1) and (id1+1 = id2)