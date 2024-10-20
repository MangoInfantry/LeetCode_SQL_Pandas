# Write your MySQL query statement below
with cte as (select coalesce(salary,null) as salary,
             dense_rank() over (order by salary desc) as ranking
             from employee
             order by ranking)

select coalesce((select salary
                 from cte
                 where ranking = 2
                 limit 1),
                 null) as SecondHighestSalary