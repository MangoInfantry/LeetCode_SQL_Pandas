# Write your MySQL query statement below
# 7일 동안 고객이 결제한 금액의 이동 평균을 계산
# 평균 금액은 소수점 둘째 자리에서 반올림
# cte에서 sum(amount)를 partition by를 날짜를 기준으로 해서 합을 구한다 
# cte 빆에서 합과 평균을 구하는데 윈도우 함수에서 현재 값과 6행 전까지의 값들을 가져와서 계산하도록 한다
# 이동 평균도 그렇게 계산하고 7로 나눈다  

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

