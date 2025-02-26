-- 판매된 모든 제품의 첫해에 대한 제품 ID, 연도, 수량 및 가격을 선택하는 솔루션을 작성합니다.
-- 결과 테이블을 임의의 순서로 반환합니다.
-- 결과 형식은 다음 예제와 같습니다.

-- cte문 안에 product_id에 따른 year의 dense_rank()를 적용시킨 후, product_id, year, quantity, price를 출력

with cte as (
    select product_id, dense_rank() over (partition by product_id order by year asc) as rnk, year, quantity, price
    from sales
)

select product_id, year as first_year, quantity, price
from cte 
where rnk = 1