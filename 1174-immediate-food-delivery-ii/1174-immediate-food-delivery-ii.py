# 고객이 선호하는 배송 날짜가 주문 날짜와 동일한 경우 즉시 주문이라고 하며, 그렇지 않은 경우 예약 주문이라고 합니다.
# 고객의 첫 번째 주문은 고객이 주문한 주문 중 주문 날짜가 가장 빠른 주문입니다. 고객에게 정확히 하나의 첫 주문이 있다는 것은 보장됩니다.
# 모든 고객의 첫 주문에서 즉시 주문의 비율을 소수점 둘째 자리에서 반올림하여 구하는 솔루션을 작성합니다.
# 결과 형식은 다음 예제와 같습니다.


import pandas as pd

def immediate_food_delivery(delivery):
    delivery['rank'] = delivery.groupby('customer_id')['order_date'].rank(method='dense')
    result = delivery[delivery['rank']==1]
    return pd.DataFrame({'immediate_percentage': [100*round((len(result[result['order_date'] == result['customer_pref_delivery_date']])/len(result)),4)]})

    
    