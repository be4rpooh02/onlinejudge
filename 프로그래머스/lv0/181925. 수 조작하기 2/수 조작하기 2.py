def solution(numLog):
    key={'1':'w', '-1':'s', '10':'d', '-10':'a'}
    prev=numLog[0]
    answer=''
    for curr in numLog[1:]:
        answer+=key[str(curr-prev)]
        prev=curr

    return answer