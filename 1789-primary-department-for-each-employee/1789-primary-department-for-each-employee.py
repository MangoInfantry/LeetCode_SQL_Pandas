# 직원은 여러 부서에 소속될 수 있습니다. 직원이 다른 부서에 합류할 때는 어느 부서를 기본 부서로 할지 결정해야 합니다. 직원이 한 부서에만 소속된 경우 기본 열은 'N'입니다.
# 모든 직원의 기본 부서를 보고하는 솔루션을 작성합니다. 한 부서에 소속된 직원의 경우, 자신의 유일한 부서만 보고합니다.
# 결과 테이블을 임의의 순서로 반환합니다.
# 결과 형식은 다음 예제와 같습니다.

import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employee['count'] = employee.groupby('employee_id')['department_id'].transform('nunique')
    return employee[(employee['count']==1) | (employee['primary_flag']=='Y')][['employee_id','department_id']]
    