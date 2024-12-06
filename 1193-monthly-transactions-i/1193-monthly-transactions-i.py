# 월별, 국가별 거래 건수 및 총액, 승인된 거래 건수 및 총액을 찾는 솔루션을 작성
# 결과 테이블을 임의의 순서로 반환

import pandas as pd
import numpy as np

def monthly_transactions(transactions):
    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')
    transactions['approved'] = np.where(transactions['state'] == 'approved',transactions['amount'],nan)
    
    trans_count = transactions.groupby(['month', 'country'])['state'].count()
    approved_count = transactions[transactions['state'] == 'approved'].groupby(['month', 'country'])['state'].count()
    trans_total_amount = transactions.groupby(['month', 'country'])['amount'].sum()
    approved_total_amount = transactions[transactions['state'] == 'approved'].groupby(['month', 'country'])['amount'].sum()
    
    table = pd.DataFrame({
        'trans_count': trans_count,
        'approved_count': approved_count,
        'trans_total_amount': trans_total_amount,
        'approved_total_amount': approved_total_amount
    }).reset_index().fillna(0)
    table['country'].replace('null',nan,inplace=True)
    return table

    