def solution(n):
    answer = 0
    for _ in range(n):
        answer+=1
        while(not answer%3 or "3" in str(answer)):
            answer+=1

    return answer