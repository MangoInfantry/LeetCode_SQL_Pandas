# Write your MySQL query statement below
with cte as (select id, temperature, recordDate,
             lag(temperature,1) over (order by recordDate) as yesterday,
             lag(recorddate,1) over (order by recordDate) as yesterdate
             from weather)

select id 
from cte
where temperature > yesterday and datediff(recordDate,yesterdate) = 1