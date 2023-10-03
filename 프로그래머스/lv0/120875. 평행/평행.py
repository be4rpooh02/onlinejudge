def solution(dots):
    answer = 0
    p1 = dots.pop(0)
    
    for i in range(3):
        rem = dots.copy()
        p2 = rem.pop(i)
        p3,p4 = rem
        
        l1 = (p1[0]-p2[0])/(p1[1]-p2[1])
        l2 = (p3[0]-p4[0])/(p3[1]-p4[1])
        
        if(l1 == l2):
            answer = 1
            break

    return answer