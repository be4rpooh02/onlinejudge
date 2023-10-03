def solution(arr, queries):
    answer = arr.copy()
    for item in queries:
        answer[item[0]], answer[item[1]] = answer[item[1]], answer[item[0]]

    return answer