def solution(emergency):
    res = list(sorted(emergency, reverse=True))
    answer = [res.index(em)+1 for em in emergency]
    return answer