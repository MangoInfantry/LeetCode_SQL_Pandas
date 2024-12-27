# 유효한 이메일을 가진 사용자를 찾는 솔루션을 작성하세요.
# 유효한 이메일에는 접두사 이름과 도메인이 있습니다:
# 접두사 이름은 문자(대/소문자), 숫자, 밑줄 '_', 마침표 '.' 및/또는 대시 '-'를 포함할 수 있는 문자열입니다. 접두사 이름은 반드시 문자로 시작해야 합니다.
# 도메인은 '@leetcode.com'입니다.
# 결과 테이블을 임의의 순서로 반환합니다.
# 결과 형식은 다음 예시와 같습니다.

import pandas as pd

def valid_emails(users):
    table = users[users['mail'].str.contains('@leetcode.com')]
    result = table[table['mail'].str.match("^[a-zA-Z][a-zA-Z0-9\.\-\_]*@leetcode\.com$")]
    return result
    