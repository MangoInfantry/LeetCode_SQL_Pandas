import pandas as pd

def department_highest_salary(employee, department):
    employee = employee.rename(columns={'name':'Employee'})
    department = department.rename(columns={'name':'Department'})
    table = pd.merge(employee, department, left_on='departmentId',right_on = 'id', how='left')
    table = table.rename(columns={'id_x':'id'}).drop(columns={'id_y'})
    temp = table.groupby(['Department'])['salary'].max().reset_index()
    table = table.merge(temp, how='inner', on = ['salary','Department'])
    table = table.rename(columns={'salary':'Salary'})
    return table[['Department','Employee','Salary']]
