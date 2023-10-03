def solution(myString, pat):
    # 풀이2 - 문자열 패턴 찾기
    revId = myString[::-1].find(pat[::-1])
    answer=myString[:len(myString)-revId]
    return answer


"""
# 풀이1 - 정규식 이용

import re

def solution(myString, pat):
    revString = myString[::-1]
    res = re.search(pat[::-1], revString).start()
    answer=revString[res::][::-1]
    return answer
"""