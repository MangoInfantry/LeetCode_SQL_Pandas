# Write your MySQL query statement below
select e.name as employee
from employee as e
join employee as emp
on e.managerid = emp.id 
where e.salary > emp.salary