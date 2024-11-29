import pandas as pd

def exchange_seats(seat):
    for i in range(1, len(seat), 2):
        seat.iloc[i-1,1], seat.iloc[i,1] = seat.iloc[i,1], seat.iloc[i-1,1]
    return seat