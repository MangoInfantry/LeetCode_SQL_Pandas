# 각 콘테스트에 등록된 사용자의 백분율을 소수점 둘째자리로 반올림
# 백분율에 따라 내림차순으로 정렬된 결과 테이블을 반환 동점인 경우 contest_id를 기준으로 오름차순으로 정렬


import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame):
    temp = register.groupby('contest_id')['user_id'].count().reset_index()
    temp['percentage'] = round(100.0 * (temp['user_id']/len(users)),2)
    temp = temp.sort_values(by=['percentage','contest_id'], ascending=[False, True])
    return temp[['contest_id','percentage']]
    