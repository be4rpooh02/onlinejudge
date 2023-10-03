def solution(lottos, win_nums):
    known=len(set(lottos).intersection(set(win_nums)))
    best = known + lottos.count(0)
    
    l = 7-known if known>0 else 6
    h = 7-best if best>0 else 6

    answer = [h, l]
    return answer