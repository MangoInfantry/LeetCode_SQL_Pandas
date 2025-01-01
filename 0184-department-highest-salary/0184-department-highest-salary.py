# 각 부서에서 가장 높은 연봉을 받는 직원을 찾는 솔루션을 작성합니다.
# 결과 테이블을 임의의 순서로 반환합니다.
# 결과 형식은 다음 예제와 같습니다.

import pandas as pd

def department_highest_salary(employee, department):
    department.rename(columns={'name':'Department'}, inplace=True)
    table = pd.merge(employee, department, left_on='departmentId', right_on='id')
    table['rank'] = table.groupby(['Department'])['salary'].rank(method='dense', ascending=False)
    result = table[table['rank']==1]
    result.rename(columns={'salary':'Salary','name':'Employee'}, inplace=True)
    return result[['Department','Employee','Salary']]
    