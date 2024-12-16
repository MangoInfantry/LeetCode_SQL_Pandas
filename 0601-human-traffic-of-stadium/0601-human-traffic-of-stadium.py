# 아이디가 연속된 행이 3개 이상이고, 각각 100명 이상인 레코드를 표시하는 솔루션을 작성하세요.
# 방문 날짜를 오름차순으로 정렬한 결과 테이블을 반환합니다.
# 결과 형식은 다음 예시와 같습니다.

import pandas as pd

def human_traffic(stadium):
    temp = stadium[stadium['people']>=100]
    temp['before_id'] = temp.id.shift()
    temp['after_id'] = temp.id.shift(-1)
    temp2 = temp[(temp.before_id + 1 == temp.id) & (temp.after_id -1 == temp.id)]
    result = temp[(temp.id.isin(temp2.before_id.unique()) | (temp.id.isin(temp2.after_id.unique())) | (temp.id.isin(temp2.id.unique())))][['id','visit_date','people']]
    return result

    