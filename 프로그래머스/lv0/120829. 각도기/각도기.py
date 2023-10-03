def solution(angle):
    first = (angle//90)*2
    second = 1 if(angle%90) else 0

    answer = first + second
    return answer