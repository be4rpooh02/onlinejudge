def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        res = len([i for m in range(1, i//2+1) if(not i%m)])
        answer += i if(res%2) else i*-1
    return answer