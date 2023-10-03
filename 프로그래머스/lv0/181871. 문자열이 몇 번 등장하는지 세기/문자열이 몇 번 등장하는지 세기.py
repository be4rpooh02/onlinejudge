def solution(myString, pat):
    idx=len(myString)-len(pat)+1
    answer = sum(int(myString[id:].startswith(pat)) for id in range(idx))
    return answer