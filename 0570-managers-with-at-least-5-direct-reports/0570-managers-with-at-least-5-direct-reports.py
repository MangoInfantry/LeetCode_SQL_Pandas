import pandas as pd

def find_managers(employee):
    id_number = employee['managerId'].value_counts()
    return employee.loc[employee['id'].isin(id_number[id_number>=5].index),['name']]
    