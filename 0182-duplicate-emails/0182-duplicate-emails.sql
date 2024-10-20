# Write your MySQL query statement below
# null 없음, 순서 상관 없음 
# cte, window , cte로 할거고 cte 내에서 email을 group by 해서 count(*) count가 2개 이상일 경우만 출력하게 만들겁니다.
with cte as (
    select id, email, count(*) as cnt
    from person
    group by email
) 

select email as Email
from cte 
where cnt>=2
