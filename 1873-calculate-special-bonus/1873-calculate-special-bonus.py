# 각 직원의 보너스를 계산하는 솔루션을 작성하십시오. 직원의 ID가 홀수이고 직원의 이름이 'M'으로 시작하지 않는 경우 직원의 보너스는 급여의 100%입니다. 그렇지 않으면 직원의 보너스는 0입니다.
# employee_id를 기준으로 정렬된 결과 테이블을 반환합니다.
# 결과 형식은 다음 예시와 같습니다.

import pandas as pd

def calculate_special_bonus(employees):
    employees['bonus'] = 0
    employees.loc[(employees['employee_id']%2==1) & (~employees['name'].str.startswith('M')),'bonus'] = employees['salary']
    return employees[['employee_id','bonus']].sort_values(by='employee_id')

    