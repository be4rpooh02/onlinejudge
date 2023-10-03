def solution(sizes):
    x,y = 0,0
    for a,b in sizes:
        if(a<b):
            a,b = b,a
        
        x = max(x,a)
        y = max(y,b)

    answer = x*y
    return answer