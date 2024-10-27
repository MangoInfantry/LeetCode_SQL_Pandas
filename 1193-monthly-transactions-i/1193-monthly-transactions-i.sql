# Write your MySQL query statement below
# 월별, 국가별 거래 건수 및 총액, 승인된 거래 건수 및 총액을 찾는 쿼리 
# month, country를 그룹화하여 trans_count, approved_count를 센다.
# trans_total_amount, approved_total_amount를 case when 구문을 써서 누적합을 계산한다.

with cte as(
    select left(trans_date,7) as month, country, state, amount 
    from transactions
)

select month, country, 
       count(*) as trans_count,
       sum(case when state = 'approved' then 1 else 0 end) as approved_count,
       sum(amount) as trans_total_amount,
       sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from cte
group by month, country