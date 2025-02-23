-- 가장 많은 친구를 가진 사람과 가장 많은 친구 수를 찾는 솔루션을 작성합니다.
-- 테스트 케이스는 한 사람만 가장 많은 친구를 보유하도록 생성됩니다.
-- 결과 형식은 다음 예제와 같습니다.
-- cte안에 union을 써서 requester_id와 accepter_id를 병합
-- union한 후, cte2에서 group by를 이용하여 id와 id 카운트를 센 후, cte2 밖에서 order by를 이용해 내림차순으로 정렬, limit 1을 이용하여 처음 id만 출력 

with cte as (
    select requester_id as id
    from requestaccepted
    union all 
    select accepter_id as id
    from requestaccepted
), cte2 as (
    select id, count(id) as num
    from cte 
    group by id
)

select id, num
from cte2
order by num desc 
limit 1

 