import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)
    temp = employee[employee['rank']==2]
    temp.rename(columns={'salary':'SecondHighestSalary'}, inplace=True)
    temp.drop_duplicates(subset='SecondHighestSalary', inplace=True)
    if not temp.empty:
        return pd.DataFrame({'SecondHighestSalary':temp['SecondHighestSalary']})
    else:
        return pd.DataFrame({'SecondHighestSalary':[None]})