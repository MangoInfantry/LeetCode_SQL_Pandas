# 판매된 모든 제품의 첫해에 대한 제품 ID, 연도, 수량 및 가격을 선택하는 솔루션을 작성합니다.
# 결과 테이블을 임의의 순서로 반환합니다.
# 결과 형식은 다음 예제와 같습니다.
# sales 테이블만 이용하면 됩니다.
# window function의 dense_rank를 이용하여 제품 별 연도를 정렬합니다.
# rnk가 1인 것만 출력하도록 합니다.  
with cte as (
    select product_id,
           dense_rank() over (partition by product_id order by year) as rnk,
           year,
           quantity,
           price
    from sales as s
)

select product_id,
       year as first_year,
       quantity,
       price
from cte
where rnk=1