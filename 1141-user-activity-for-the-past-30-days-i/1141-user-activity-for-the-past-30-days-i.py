# 2019-07-27을 포함하여 30일 동안의 일일 활성 사용자 수를 구하는 솔루션을 작성하세요. 사용자가 해당 날짜에 최소 한 번 이상 활동을 했다면 해당 사용자는 하루 동안 활동한 것입니다.
# 결과 테이블은 임의의 순서로 반환합니다.
# 결과 형식은 다음 예제와 같습니다.

import pandas as pd

def user_activity(activity):
    activity = activity[(activity['activity_date'] >='2019-06-28') & (activity['activity_date'] <= '2019-07-27')]
    table = activity.groupby('activity_date')['user_id'].nunique().reset_index()
    table.rename(columns={'activity_date':'day', 'user_id':'active_users'}, inplace=True)
    return table
    