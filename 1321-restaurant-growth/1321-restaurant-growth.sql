# Write your MySQL query statement below
# 7일 동안 고객이 결제한 금액의 이동 평균을 계산
# 평균 금액은 소수점 둘째 자리에서 반올림
# visited_on을 기준으로 lead(6)을 해서 7일치의 데이터를 가지고 온다.
# 데이터를 가지고 오면 그 구간에 있는 데이터들을 
# 날짜를 기준으로 나열해서 rank가 7인 것까지 추출한 뒤, 합계를 구한다 

with cte as (
    select distinct visited_on,
           sum(amount) over (partition by visited_on) as sum_amount
    from customer
), 
cte2 as (
    select distinct visited_on,
       sum(sum_amount) over (order by visited_on rows between 6 preceding and current row) as amount,
       round(sum(sum_amount) over (order by visited_on rows between 6 preceding and current row)/7,2) as average_amount,
       lag(visited_on,6) over (order by visited_on) as lag6
    from cte
)

select visited_on, amount, average_amount
from cte2
where lag6 is not null

