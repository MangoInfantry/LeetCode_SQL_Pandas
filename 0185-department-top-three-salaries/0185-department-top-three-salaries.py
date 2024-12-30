# 회사의 경영진은 회사의 각 부서에서 누가 가장 많은 돈을 버는지 알고 싶어 합니다. 한 부서의 고소득자는 해당 부서의 고유 연봉 상위 3개에 속하는 직원을 의미합니다.
# 각 부서에서 고소득 직원을 찾는 솔루션을 작성합니다.
# 결과 테이블을 임의의 순서로 반환합니다.
# 결과 형식은 다음 예제와 같습니다.

import pandas as pd

def top_three_salaries(employee,department):
    table = pd.merge(employee, department, left_on = 'departmentId', right_on='id')
    table.rename(columns={'name_y':'Department', 'name_x':'Employee','salary':'Salary'},inplace=True)
    table['rank'] = table.groupby('Department')['Salary'].rank(method='dense', ascending=False)
    return table[table['rank']<=3][['Department','Employee','Salary']]