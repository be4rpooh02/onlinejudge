def solution(participant, completion):
    answer = ""
    lpar = {}

    if not completion:
        answer = participant[0]
        return answer
    
    for p in participant:
        lpar[p] = lpar[p]+1 if p in lpar.keys() else 1
    
    for c in completion:
        lpar[c] = lpar[c]-1
        
        if not lpar[c]:
            del lpar[c]
    
    answer = list(lpar)[0]

    return answer