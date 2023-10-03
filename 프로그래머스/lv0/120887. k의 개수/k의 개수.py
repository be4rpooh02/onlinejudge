def solution(i, j, k):
    answer = ''.join([str(num) for num in range(i,j+1)]).count(str(k))
    return answer