def solution(word):
    from itertools import product
    res = []
    answer = 0
    
    t = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(1, len(t)+1):
        res += product(t, repeat=i)
    
    for idx, w in enumerate(sorted(res)):
        if "".join(w) == word:
            answer = idx+1

    return answer