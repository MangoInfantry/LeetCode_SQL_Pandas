# Write your MySQL query statement below
# 출력: 아이디가 연속된 행이 3개 이상, 각각 100명 이상인 레코드를 표시하는 솔루션
# 조건: 방문 날짜를 오름차순으로 정렬해야 함 
# 100명 이상이어야 출력할 수 있으므로, cte에서 100명 넘은 날만 출력할 수 있도록 필터링 
# cte에 앞이나 뒤의 순번이 연속적인지를 확인하기 위해 lag, lead를 활용한다. 


with cte as (
    select id,
           visit_date,
           people,
           lag(people,2) over () as lag1,
           lag(people,1) over () as lag2,
           lead(people,1) over () as lead1,
           lead(people,2) over () as lead2
      from stadium
)

select id, visit_date, people
from cte
where people>=100 and ((lag1 >=100 and lag2 >= 100) or (lead1 >= 100 and lead2 >= 100) or (lag2 >= 100 and lead1 >= 100))


