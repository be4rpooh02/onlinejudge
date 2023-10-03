def solution(spell, dic):
    answer = 2
    for item in dic:
        if(set(spell) == set(item)):
            answer=1
            break
    return answer