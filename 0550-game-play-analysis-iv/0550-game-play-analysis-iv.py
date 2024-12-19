# 처음 로그인한 날의 다음 날에 다시 로그인한 플레이어의 비율을 소수점 둘째 자리에서 반올림하여 보고하는 솔루션을 작성하세요. 즉, 첫 로그인 날짜부터 최소 이틀 연속 로그인한 플레이어 수를 계산한 다음 그 수를 전체 플레이어 수로 나누면 됩니다.
# 결과 형식은 다음 예시와 같습니다.

import pandas as pd

def gameplay_analysis(activity):
    activity['first_date'] = activity.groupby('player_id')['event_date'].transform('min')
    activity['day_diff'] = (activity['event_date'] - activity['first_date']).dt.total_seconds() == 86400
    result = round(len(activity[activity['day_diff'] == True])/len(activity.drop_duplicates(subset='player_id')),2)
    result_table = pd.DataFrame({'fraction':[result]})
    return result_table
    