def solution(numbers):
    res = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    answer = str(int("".join(res)))
    
    return answer