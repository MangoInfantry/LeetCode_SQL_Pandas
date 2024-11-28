# 출력: 점수와 점수에 따른 랭킹 (scores, rank)
# 조건: 동점일 경우 다음 순위 번호는 연속된 다음 정수, 즉, 부여된 순위가 숫자를 뛰어 넘으면 안됨 무조건 연속적, 점수 순으로 내림차순 정렬
import pandas as pd

def order_scores(scores):
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    dense_rank_df = scores.drop(columns=['id']).sort_values(by='score', ascending=False)
    return dense_rank_df

    