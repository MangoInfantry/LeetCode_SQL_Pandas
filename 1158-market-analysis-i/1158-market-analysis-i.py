import pandas as pd
# 출력: 2019년도에 구매자로서 주문한 주문 수에 대해 솔루션을 작성

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders = orders[orders.order_date.dt.year==2019]
    table1 = pd.merge(users, orders, left_on= 'user_id', right_on='buyer_id', how='left')
    table2 = pd.merge(table1, items, on='item_id', how='left')
    result = table2.groupby(['user_id','join_date'])['order_id'].count().reset_index().rename(columns={'user_id':'buyer_id', 'order_id':'orders_in_2019'})
    return result

