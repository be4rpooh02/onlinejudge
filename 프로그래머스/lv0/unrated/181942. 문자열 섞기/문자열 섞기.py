def solution(str1, str2):
    answer = ''.join(ch[0]+ch[1] for ch in zip(str1, str2))
    return answer