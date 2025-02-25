# Write your MySQL query statement below
-- 고객이 선호하는 배송 날짜가 주문 날짜와 동일한 경우 즉시 주문이라고 하며, 그렇지 않은 경우 예약 주문이라고 합니다.
-- 고객의 첫 주문은 고객이 주문한 주문 중 주문 날짜가 가장 빠른 주문입니다. 고객에게 정확히 하나의 첫 주문이 있다는 것은 보장됩니다.
-- 모든 고객의 첫 주문에서 즉시 주문의 비율을 소수점 둘째 자리에서 반올림하여 구하는 솔루션을 작성합니다.
-- 결과 형식은 다음 예제와 같습니다.

-- first order이 즉시 배송인지, 아니면 예약 배송인지 확인해야하기 때문에, dense_rank() 윈도우 함수를 매겨서 1순위인 것만 뽑아냄
-- first order의 sum(case when ~ ) 을 이용해서 order_date가 customer_pref_delivery_date와 같은 지 조건걸어서 한 다음, 총 주문 개수로 나눠서 퍼센트 출력

with cte as (
    select order_date, customer_pref_delivery_date, dense_rank() over (partition by customer_id order by order_date) as rnk  
    from delivery
)

select 100.0 * round(sum(case when order_date = customer_pref_delivery_date then 1 else 0 end)/count(*),2) as immediate_percentage
from cte
where rnk = 1 