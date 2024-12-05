# 7일 동안(즉, 현재일 + 6일 전) 고객이 결제한 금액의 이동 평균을 계산합니다. 평균_금액은 소수점 둘째 자리에서 반올림해야 합니다.
# visited_on을 기준으로 오름차순으로 정렬된 결과 테이블을 반환합니다.
# .rolling 메소드는 시계열이나 순차 데이터에서 사용되는 이동평균을 구할 수 있는 메소드 


import pandas as pd

def restaurant_growth(customer: pd.DataFrame):
    customer = customer.groupby('visited_on')['amount'].sum().reset_index()
    customer['rolling_sum'] = round(customer['amount'].rolling(7).mean(),2)
    customer['amount_sum'] = round(customer['amount'].rolling(7).sum(),2)
    customer.drop(columns=['amount'], inplace=True)
    customer.rename(columns={'rolling_sum':'average_amount', 'amount_sum':'amount'}, inplace=True)
    customer = customer.dropna()
    return customer[['visited_on','amount','average_amount']]