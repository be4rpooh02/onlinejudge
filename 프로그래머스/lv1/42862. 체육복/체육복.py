def solution(n, lost, reserve):
    sl, sr = set(lost), set(reserve)
    sboth = sl.intersection(sr)
    slost = sl.difference(sboth)
    sreserve = sr.difference(sl)

    answer = n-len(lost)+len(sboth)
    
    for l in slost:
        can = set([l-1, l+1]).intersection(sreserve)
        
        if can:
            answer+=1
            sreserve.remove(min(can))

    return answer