# Write your MySQL query statement below
# 가장 많은 수의 영화에 별점을 준 사용자의 이름을 찾기 동점인 경우 사전적으로 더 순서가 낮은 이름을 반환
# 2020년 2월에 평균 평점이 가장 높은 영화 이름, 동점일 경우 사전적으로 더 순서가 낮은 이름을 반환
# cte1에서 users와 movierating 테이블을 조인한다 -> 그다음 group by를 써서 name과 name의 카운트를 출력한다. 
# cte2에서 movies와 movierating 테이블을 조인한다 -> 그다음 group by를 써서 평균 평점을 구한다.
# 두 테이블을 union all한다.

with cte as (
    select name, count(name) as cnt 
    from users as u
    join movierating as m 
    on u.user_id = m.user_id
    group by name
    order by cnt desc, name asc
    limit 1
), 
cte2 as (
    select title, avg(rating) as avg_rate
    from movies as m
    join movierating as r
    on m.movie_id = r.movie_id
    where left(created_at,7) = '2020-02'
    group by title
    order by avg_rate desc, title asc 
    limit 1
)


select name as results 
from cte

union all 

select title
from cte2
