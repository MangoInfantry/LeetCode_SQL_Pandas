import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    before = products[products['change_date']<='2019-08-16']
    before['rank'] = before.groupby('product_id')['change_date'].rank(ascending=False)
    before = before[before['rank']==1].rename(columns={'new_price':'price'})
    temp = products[~products['product_id'].isin(before['product_id'])]
    temp['new_price'] = 10
    temp = temp.rename(columns={'new_price':'price'})
    table = pd.concat([before, temp]).drop_duplicates(subset='product_id')
    table = table.sort_values(by='product_id')[['product_id','price']]
    return table