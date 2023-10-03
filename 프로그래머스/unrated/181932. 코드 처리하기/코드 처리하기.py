def solution(code):
    mode = 0
    answer = ""
    
    for idx, ch in enumerate(code):
        if(ch == '1'):
            mode=0 if(mode) else 1
            continue

        if mode%2 == idx%2:
            answer+=ch            
        
    return answer if(answer) else "EMPTY"