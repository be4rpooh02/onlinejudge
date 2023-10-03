def solution(q, r, code):
    # 풀이 1
    # answer = ''.join([ch for idx, ch in enumerate(code) if(idx%q==r)])
    
    # 풀이2
    answer = code[r::q]
    
    return answer