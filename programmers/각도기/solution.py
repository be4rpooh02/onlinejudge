// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120829

def solution(angle):
    first = (angle//90)*2
    second = 1 if(angle%90) else 0

    answer = first + second
    return answer