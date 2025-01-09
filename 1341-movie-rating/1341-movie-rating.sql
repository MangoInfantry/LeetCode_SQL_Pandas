# Write your MySQL query statement below
# 가장 많은 수의 영화에 별점을 준 사용자의 이름을 찾습니다. 동점인 경우 사전적으로 더 작은 사용자 이름을 반환합니다.
# 2020년 2월에 평균 평점이 가장 높은 영화 이름을 찾습니다. 동점일 경우 사전적으로 더 작은 영화 이름을 반환합니다.
# 결과 형식은 다음 예시와 같습니다.

# 이름과 window function을 이용하여 이름이 몇번 세어졌는지를 첫번째 cte문으로 한다.  
with cte as (
    select distinct name, count(name) over (partition by name) as cnt
    from users as u
    right join movierating as m
    on u.user_id = m.user_id
    order by cnt desc, name
    limit 1
), cte2 as (
    select distinct title, avg(rating) over (partition by title) as rate
    from movierating as r
    left join movies as m
    on r.movie_id = m.movie_id
    where left(created_at, 7) = '2020-02'
    order by rate desc, title 
    limit 1
)

select name as results 
from cte

union all 

select title
from cte2
