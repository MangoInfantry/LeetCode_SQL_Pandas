# 버스 탑승을 기다리는 사람들이 줄을 서 있습니다. 하지만 버스의 무게 제한이 1000킬로그램이므로 탑승할 수 없는 사람이 있을 수 있습니다.
# 체중 제한을 초과하지 않고 버스에 탈 수 있는 마지막 사람의 person_name을 찾는 솔루션을 작성하세요. 테스트 케이스는 첫 번째 사람이 체중 제한을 초과하지 않도록 생성됩니다.
# 한 번에 한 사람만 버스에 탑승할 수 있다는 점에 유의하세요.
# 결과 형식은 다음 예시와 같습니다.

import pandas as pd

def last_passenger(queue):
    queue = queue.sort_values(by= 'turn')
    queue['total_weight'] = queue['weight'].cumsum()
    over_1000 = queue[queue['total_weight']<=1000]
    weight_1 = over_1000.sort_values(by='total_weight', ascending=False).head(1)['person_name'].to_frame()
    return weight_1

    