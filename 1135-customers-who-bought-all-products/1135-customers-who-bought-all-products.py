import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    temp = customer.groupby('customer_id')[['product_key']].nunique().reset_index()
    temp = temp[temp['product_key']==len(product)][['customer_id']]
    return temp