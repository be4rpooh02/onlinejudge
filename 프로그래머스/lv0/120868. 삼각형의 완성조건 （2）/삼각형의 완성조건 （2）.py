def solution(sides):
    #answer = len(range(abs(sides[1]-sides[0])+1,sides[0]+sides[1]))
    answer = 2*min(sides)-1
    return answer