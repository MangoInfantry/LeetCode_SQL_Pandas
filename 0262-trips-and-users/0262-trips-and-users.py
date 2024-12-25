# 취소율은 금지되지 않은 사용자로 인해 취소된 (클라이언트 또는 드라이버별) 요청 수를 해당 날짜의 금지되지 않은 사용자로 인한 총 요청 수로 나누어 계산합니다.
# “2013-10-01"과 ‘2013-10-03’ 사이의 매일 금지되지 않은 사용자(클라이언트와 드라이버 모두 금지되지 않아야 함)가 있는 요청의 취소율을 구하는 솔루션을 작성하세요. 취소율은 소수점 둘째 자리에서 반올림합니다.
# 결과 테이블을 임의의 순서로 반환합니다.
# 결과 형식은 다음 예시와 같습니다.
# cancel된 것들의 비율 구해라. 
# 단, banned된 것들은 전체 합산에서 제외한다. 

import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    table = pd.merge(trips, users, left_on='client_id', right_on='users_id', how='left')
    table = table[(table['request_at'] >= '2013-10-01') & (table['request_at'] <= '2013-10-03')].rename(columns={'request_at': 'Day'})
    not_banned_count = table[table['banned'] == 'No']
    not_banned_count['Cancelled'] = not_banned_count['status'].str.startswith('can')
    cancel_rate = round(not_banned_count.groupby('Day')['Cancelled'].sum()/not_banned_count.groupby('Day')['id'].count(),2)
    not_banned_count = not_banned_count.merge(cancel_rate.rename('Cancellation Rate'), on='Day')
    not_banned_count.drop_duplicates(subset=['Day','Cancellation Rate'], inplace=True)
    return not_banned_count[['Day','Cancellation Rate']]

    