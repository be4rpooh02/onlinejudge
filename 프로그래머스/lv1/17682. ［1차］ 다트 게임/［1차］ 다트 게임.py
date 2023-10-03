def solution(dartResult):
    import re
    scores = re.findall('(\d+)([SDT])([*#]?)', dartResult)

    bonus = {"S": 1,"D": 2,"T": 3}
    opts = {"": 1,"*": 2,"#": -1}
    res = []
    
    for idx, item in enumerate(scores):
        res.append(int(item[0])**bonus[item[1]]*opts[item[2]])
        
        if item[2] == "*" and idx > 0:
            res[idx-1] = res[idx-1]*2
    
    answer = sum(res)

    return answer