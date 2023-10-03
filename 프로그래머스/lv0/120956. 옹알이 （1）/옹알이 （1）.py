def solution(babbling):
    s = ["woo", "aya", "ma", "ye"]
    answer = 0
    for w in babbling:
        for c in s:
            w = w.replace(c, " ")
        if(not w.strip()):
            answer+=1
    
    return answer