def solution(strArr):
    answer = [item[1].upper() if(item[0]%2) else item[1].lower() for item in enumerate(strArr)]
    return answer