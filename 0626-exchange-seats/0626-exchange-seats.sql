# Write your MySQL query statement below
# 자리를 스왑하는 문제 
# 1~2, 3~4, 5~6 ... 순서로 근데, 마지막 자리가 홀수면 스왑 안함
# case when을 활용해서 풀면 될 것 같다. (먼저 최대 수 홀수일 때만 id로 출력, id가 홀수일 때 id를 짝수, id가 짝수일 때, id를 홀수로 변환)

select (case when id%2=1 and id = (select max(id) from seat) then id
            when id%2=1 then id+1
            when id%2=0 then id-1 end) as id, 
            student 
from seat
order by id
