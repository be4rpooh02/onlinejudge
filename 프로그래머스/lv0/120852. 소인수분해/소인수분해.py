def solution(n):
    d = 2
    answer = []
    while d<=n:
        if(not n%d):
            if(d not in answer):
                answer.append(d)
            n=n//d
        else:
            d+=1
    return answer