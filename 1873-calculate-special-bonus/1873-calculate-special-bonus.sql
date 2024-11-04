# Write your MySQL query statement below
# 출력: 각 직원의 보너스를 계산하는 솔루션을 작성
# 조건: 직원의 ID가 홀수이고 직원의 이름이 'M'으로 시작하지 않는 경우 직원의 보너스는 급여의 100%입니다. 그렇지 않으면 직원의 보너스는 0
# cte에서 전체에서 M으로 시작하지 않고, 홀수인 거를 뺀다
# cte문 밖에서 전체에서 M으로 시작하지 않고, 홀수인 거를 합집합으로 다시 더해준다. 

with cte as(
    select employee_id, 0 as bonus
    from employees

    except

    select employee_id, 0 as bonus
    from employees
    where employee_id%2=1 and name not like 'M%'
)

select *
from cte
union all

select employee_id, salary as bonus
from employees
where employee_id%2=1 and name not like 'M%'
order by employee_id