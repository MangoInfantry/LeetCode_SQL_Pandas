# 단일 숫자는 내 번호 테이블에 한 번만 표시된 숫자입니다.
# 가장 큰 단일 숫자를 찾습니다. 단일 숫자가 없는 경우 null을 보고합니다.
# 결과 형식은 다음 예시와 같습니다.

import pandas as pd

def biggest_single_number(my_numbers):
    table = my_numbers['num'].value_counts().reset_index()
    value = table[table['count']==1]['num'].sort_values(ascending=False)
    if not value.empty:
        return pd.DataFrame({'num': value.head(1)})
    else:
        return pd.DataFrame({'num':[None]})
    return value
    