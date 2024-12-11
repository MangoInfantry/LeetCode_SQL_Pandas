# 사용자의 확인율은 '확인된' 메시지 수를 요청된 총 확인 메시지 수로 나눈 값입니다. 확인 메시지를 요청하지 않은 사용자의 확인 비율은 0입니다. 확인 비율은 소수점 둘째 자리에서 반올림합니다.
# 각 사용자의 확인율을 구하는 솔루션을 작성합니다.
# 결과 테이블을 임의의 순서로 반환합니다.
# 결과 형식은 다음 예제와 같습니다.

import pandas as pd

def confirmation_rate(signups, confirmations):
    table = pd.merge(signups, confirmations,  how='left', on='user_id')
    temp1 = table[table['action']=='confirmed'].groupby(['user_id'])['action'].count().reset_index().rename(columns={'action_x':'confirm_count'})
    temp2 = table.groupby(['user_id'])['action'].count().reset_index()
    temp = pd.merge(temp1, temp2, on='user_id', how='right').rename(columns={'action_x':'confirm_count','action_y':'count'})
    temp['confirmation_rate'] = round(temp['confirm_count']/temp['count'],2)
    temp.drop_duplicates(subset='user_id', inplace=True)
    return temp[['user_id','confirmation_rate']].fillna(0)

    