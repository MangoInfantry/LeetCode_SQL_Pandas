# Write your MySQL query statement below
with cte as (select e.id as id,
                    e.name as name,
                    salary,
                    departmentId,
                    d.name as department,
                    dense_rank() over (partition by departmentId order by salary desc) as ranking
                    from department as d
                    join employee as e
                    on d.id = e.departmentId)

select department, name as employee, salary
from cte
where ranking = 1 