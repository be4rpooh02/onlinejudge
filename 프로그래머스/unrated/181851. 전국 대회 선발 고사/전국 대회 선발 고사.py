def solution(rank, attendance):
    atts=sorted([item for item in rank if attendance[rank.index(item)]])[:3]
    answer = rank.index(atts[0])*10000+rank.index(atts[1])*100+rank.index(atts[2])
    return answer