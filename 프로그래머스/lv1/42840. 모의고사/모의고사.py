def solution(answers):
    la = len(answers)

    p = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    l = [len(p[0]), len(p[1]), len(p[2])]
    
    res = [0, 0, 0]
    
    for idx, s in enumerate(answers):
        for i in range(len(res)):
            res[i] += 1 if(s == p[i][idx%l[i]]) else 0
    
    answer = [i+1 for i, x in enumerate(res) if x == max(res)]

    return answer