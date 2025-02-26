# Write your MySQL query statement below
# 취소 수/금지되지 않은 요청 비율 반환하기
# 금지되지 않은 요청 세기
# banned가 안된 유저 먼저 필터링
# banned가 안된 유저에 client_id와 driver_id 둘다 있어야함
# 
with cte as(
    select users_id from users
    where banned = 'no'
)

select request_at as Day, round(sum(case when status like 'cancelled%' then 1 else 0 end)/count(*),2) as 'Cancellation Rate'
from trips
where client_id in (select users_id from cte) and driver_id in (select users_id from cte) and request_at between '2013-10-01' and '2013-10-03'
group by request_at


