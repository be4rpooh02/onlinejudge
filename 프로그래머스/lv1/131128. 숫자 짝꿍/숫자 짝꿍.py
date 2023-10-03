def solution(X, Y):
    answer = ""
    both = set(X).intersection(set(Y))
    
    if not both:
        return "-1"
    
    la = [0]*10
    lb = la.copy()
    
    for num in X:
        la[int(num)]+=1
    
    for num in Y:
        lb[int(num)]+=1
        
    for idx, (a, b) in enumerate(zip(la, lb)):
        if a < 1 or b < 1:
            continue
        answer = str(idx)*min(a, b) + answer

    answer = "0" if answer.startswith("0") else answer    
    return answer