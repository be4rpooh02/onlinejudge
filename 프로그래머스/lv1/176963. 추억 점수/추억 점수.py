def solution(name, yearning, photo):
    yearns = dict(zip(name, yearning))
    answer = []
    
    for item in photo:
        res = sum(yearns[n] for n in set(name).intersection(set(item)))
        answer.append(res)
    return answer