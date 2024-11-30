import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    num1 = request_accepted['requester_id'].value_counts()
    num2 = request_accepted['accepter_id'].value_counts()
    #.add 메소드는 시리즈에서만 쓸 수 있는 메소드로 인덱스가 같은 경우 시리즈에 값을 추가해 줄 수 있다. (ex. 원래는 num1에 1만 있었는데 num2에 2가 있다 그러면 합치면 3)
    num = num1.add(num2, fill_value=0)
    result = num.reset_index().rename(columns={'index':'id','count':'num'}).sort_values(by='num', ascending=False)
    result = result.head(1)
    return result