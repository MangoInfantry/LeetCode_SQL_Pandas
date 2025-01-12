# Write your MySQL query statement below
# 출력: 각 직원의 보너스를 계산하는 솔루션을 작성
# 조건: 직원의 ID가 홀수이고 직원의 이름이 'M'으로 시작하지 않는 경우 직원의 보너스는 급여의 100%입니다. 그렇지 않으면 직원의 보너스는 0
# case when 문을 사용하여 홀수, 그리고 'M'으로 시작하지 않는 이름의 경우에만 필터링하여 salary를 지급하고 아닌 경우는 0으로 하도록.. 

select employee_id,
       case when employee_id%2=1 and name not like 'M%' then salary else 0 end as bonus
from employees
order by employee_id

