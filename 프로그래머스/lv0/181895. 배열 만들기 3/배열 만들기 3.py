def solution(arr, intervals):
    answer=[]
    for item in intervals:
        answer += arr[item[0]:item[1]+1]
    return answer