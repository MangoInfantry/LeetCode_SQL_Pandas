# 가장 많은 수의 영화에 별점을 준 사용자의 이름을 찾습니다. 동점인 경우 사전적으로 더 작은 사용자 이름을 반환합니다.
# 2020년 2월에 평균 평점이 가장 높은 영화 이름을 찾습니다. 동점일 경우 사전적으로 더 작은 영화 이름을 반환합니다.
# 결과 형식은 다음 예시와 같습니다.
# 각각 이름, 영화를 찾고 데이터 프레임 형태로 만들어준 다음에 pd.concat

import pandas as pd

def movie_rating(movies, users, movie_rating):
    temp1 = pd.merge(movie_rating, users, on='user_id', how='left')
    temp2 = pd.merge(temp1, movies, on='movie_id')
    temp2['year'] = temp2['created_at'].dt.year
    temp2['month'] = temp2['created_at'].dt.month
    result1 = temp2.groupby('name')['movie_id'].count().reset_index().sort_values(by=['movie_id','name'], ascending=[False,True])['name'].iloc[0]
    result1 = pd.DataFrame({'results':[result1]})
    result2 = temp2[(temp2['year']==2020) & (temp2['month']==2)]
    result2 = result2.groupby('title')['rating'].mean().reset_index().sort_values(by=['rating','title'], ascending=[False,True])['title'].iloc[0]
    result2 = pd.DataFrame({'results':[result2]})
    result = pd.concat([result1,result2])
    return result

    