# 이 문제에서는 관리자를 자신에게 보고하는 다른 직원이 1명 이상 있는 직원으로 간주하겠습니다.
# 모든 관리자의 아이디와 이름, 직접 보고하는 직원의 수, 보고자의 평균 연령을 가장 가까운 정수로 반올림하여 보고하는 솔루션을 작성합니다.
# employee_id를 기준으로 정렬된 결과 테이블을 반환합니다.
import pandas as pd
import numpy as np

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    average_age = employees.groupby('reports_to')['age'].mean().reset_index()
    reports_count = employees['reports_to'].value_counts().reset_index()
    temp = pd.merge(average_age, reports_count, on='reports_to')
    table = pd.merge(temp, employees, how='left', left_on='reports_to', right_on='employee_id')
    table.rename(columns={'count': 'reports_count', 'age_x': 'average_age'}, inplace=True)
    table['average_age'] = np.round(table['average_age'] + 0.5 * (table['average_age'] % 1 == 0.5))
    return table[['employee_id', 'name', 'reports_count', 'average_age']]

    