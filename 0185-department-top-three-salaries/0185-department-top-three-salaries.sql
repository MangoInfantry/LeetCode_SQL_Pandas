# Write your MySQL query statement below
with cte as (select d.name as department,
                    e.name as employee,
                    salary,
                    dense_rank() over (partition by d.name order by salary desc) as ranking  
from employee as e
join department as d
on e.departmentId = d.id)

select department, employee, salary
from cte
where ranking<=3