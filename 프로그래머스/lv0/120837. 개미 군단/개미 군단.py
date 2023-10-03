def solution(hp):
    answer,mod=[], 5
    
    while(hp):
        v,hp = divmod(hp, mod)
        answer.append(v)
        mod-=2

    return sum(answer)