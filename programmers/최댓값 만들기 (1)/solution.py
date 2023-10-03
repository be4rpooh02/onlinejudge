// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120847

def solution(numbers):
    #m=numbers.pop(numbers.index(max(numbers)))
    #n=max(numbers)
    m,n = numbers[0],0
    for i in numbers[1:]:
        if(i>m):
            m,n = i,m
        elif(i>=n):
            n = i
        else:
            continue

    answer = m*n
    return answer