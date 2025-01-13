# Write your MySQL query statement below
# 확인된 메세지의 비율 구하는 문제
# 사용자의 확인율은 '확인된' 메시지 수를 요청된 총 확인 메시지 수로 나눈 값입니다. 확인 메시지를 요청하지 않은 사용자의 확인 비율은 0입니다. 확인 비율은 소수점 둘째 자리에서 반올림합니다.
# 각 사용자의 확인율을 구하는 솔루션을 작성합니다.
# 결과 테이블을 임의의 순서로 반환합니다.
# 결과 형식은 다음 예제와 같습니다.

# cte테이블에서 두 테이블을 signups를 기준으로 조인한다음, case when 문을 사용하여 confirmed라고 되어있는 컬럼만 1로 바꿔준다.
with cte as (
    select s.user_id, 
           s.time_stamp,
           case when action like 'confirmed' then 1 else 0 end as confirm
    from signups as s
    left join confirmations as c
    on s.user_id = c.user_id
)

#cte문 밖에서 group by를 사용하여 user_id를 기준으로 묶어준 뒤, 비율을 구해준다.  
select user_id, round(sum(confirm)/count(user_id),2) as confirmation_rate
from cte
group by user_id
order by confirmation_rate asc, user_id 
