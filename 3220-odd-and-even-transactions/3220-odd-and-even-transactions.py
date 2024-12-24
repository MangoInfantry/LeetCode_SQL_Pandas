# 각 날짜의 홀수 거래와 짝수 거래의 금액 합계를 구하는 솔루션을 작성합니다. 특정 날짜에 홀수 또는 짝수 트랜잭션이 없는 경우 0으로 표시합니다.
# 결과 테이블을 트랜잭션_날짜를 기준으로 오름차순으로 정렬하여 반환합니다.
# 결과 형식은 다음 예시와 같습니다.

import pandas as pd

def sum_daily_odd_even(transactions):
    temp = transactions.copy()
    temp.loc[temp['amount']%2==0, 'amount'] = 0
    odd_sum = temp.groupby('transaction_date')['amount'].sum().reset_index()
    odd_sum.rename(columns={'amount':'odd_sum'}, inplace=True)
    transactions.loc[transactions['amount']%2==1, 'amount'] = 0
    even_sum = transactions.groupby('transaction_date')['amount'].sum().reset_index()
    even_sum.rename(columns={'amount':'even_sum'}, inplace=True)
    result = pd.merge(odd_sum, even_sum, on='transaction_date')
    return result
    