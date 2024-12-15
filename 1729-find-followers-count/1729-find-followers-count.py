import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    temp = followers.groupby('user_id')['follower_id'].count().reset_index()
    temp.rename(columns={'follower_id':'followers_count'}, inplace=True)
    return temp
    