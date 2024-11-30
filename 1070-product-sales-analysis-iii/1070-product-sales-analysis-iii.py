# 판매된 모든 제품의 첫해에 대한 제품 ID, 연도, 수량 및 가격을 선택하는 솔루션을 작성합니다.
# 결과 테이블을 임의의 순서로 반환합니다.

import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(sales, product, on='product_id')
    result['rank'] = result.groupby('product_id')['year'].rank(method='dense')
    result = result[result['rank']==1][['product_id','year','quantity','price']].rename(columns={'year':'first_year'})
    return result