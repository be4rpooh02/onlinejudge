// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120830

def solution(n, k):
    answer = n * 12000 + (k - n//10) * 2000
    return answer