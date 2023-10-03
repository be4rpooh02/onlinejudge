def solution(score):
    avgs = [sum(num)/len(num) for num in score]
    ranks = sorted(avgs, reverse=True)
    
    answer=[ranks.index(avg)+1 for avg in avgs]
    
    return answer