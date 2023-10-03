def solution(arr, divisor):
    res = [num for num in arr if(not num%divisor)]
    answer = sorted(res) if(len(res)) else [-1]
    return answer