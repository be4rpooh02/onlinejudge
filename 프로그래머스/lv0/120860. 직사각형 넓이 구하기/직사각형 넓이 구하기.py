def solution(dots):
    maxw,maxh = max(dots)
    minw,minh = min(dots)
    
    answer = abs((maxw-minw)*(maxh-minh))
    return answer