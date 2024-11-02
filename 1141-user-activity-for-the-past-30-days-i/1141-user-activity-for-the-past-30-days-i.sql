# Write your MySQL query statement below
# 2019년 끝나는 날짜 7월 27일을 포함해서 30일 동안 일일 활성 사용자 수를 구하는 솔루션을 작성. 
# 사용자가 해당 날짜에 최소 한 번 이상 했다면, 사용자는 하루동안 활동한 것으로 취급.
# date_sub를 이용해서 7월 27일 이전의 날짜와 7월 27일 사이의 결과만 나올 수 있도록 where을 통해 필터링, 그리고 group by activity_date, count(distinct user_id)

select activity_date as day, count(distinct user_id) as active_users 
from activity
where activity_date between date_sub('2019-07-27', interval 30 day) and '2019-07-27'
group by activity_date
