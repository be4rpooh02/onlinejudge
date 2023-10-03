def solution(n):
    #answer = [int(ch) for ch in str(n)[::-1]]
    answer = list(map(int, str(n)[::-1]))
    return answer