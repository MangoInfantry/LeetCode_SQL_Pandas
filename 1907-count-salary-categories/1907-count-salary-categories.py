# 각 급여 범주에 대한 은행 계좌 수를 계산하는 솔루션을 작성하세요. 급여 카테고리는 다음과 같습니다:
# “낮은 급여": 모든 급여가 $20000 미만입니다.
# “평균 급여": 포함 범위[$20000, $50000]의 모든 급여입니다.
# “높은 연봉": $50000보다 엄격하게 큰 모든 급여.
# 결과 테이블에는 세 가지 카테고리가 모두 포함되어야 합니다. 한 카테고리에 계정이 없는 경우 0을 반환합니다.
# 결과 테이블은 어떤 순서로든 반환합니다.
# 결과 형식은 다음 예시와 같습니다.

import pandas as pd

def count_salary_categories(accounts):
    low_income = len(accounts[accounts['income']<20000].drop_duplicates())
    average_income = len(accounts[(accounts['income']>=20000) & (accounts['income']<=50000)].drop_duplicates())
    high_income = len(accounts[accounts['income']>50000].drop_duplicates())
    result = pd.DataFrame({'category':['Low Salary','Average Salary', 'High Salary'], 'accounts_count':[low_income, average_income, high_income]})
    return result 