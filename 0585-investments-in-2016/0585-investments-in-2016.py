# 2016년의 모든 보험 계약자에 대해 2016년의 모든 총 투자 가치의 합계를 보고하는 솔루션을 작성하십시오:
# 하나 이상의 다른 보험 계약자와 동일한 tiv_2015 값을 가지며, 그리고 다른 보험계약자와 같은 도시에 있지 않아야 합니다(즉, (위도, 경도) 속성 쌍이 고유해야 함).
# tiv_2016을 소수점 이하 두 자리로 반올림합니다.
# 결과 형식은 다음 예시와 같습니다.


import pandas as pd

def find_investments(insurance):
    insurance['count'] = insurance.groupby('tiv_2015')['pid'].transform('count')
    insurance['lat_count'] = insurance.groupby(['lat', 'lon'])['pid'].transform('nunique')
    value = insurance[(insurance['lat_count']==1) & (insurance['count']>1)]['tiv_2016'].sum()
    result = pd.DataFrame({'tiv_2016':[value]})
    return result