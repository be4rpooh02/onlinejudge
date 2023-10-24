def solution(progresses, speeds):
    from math import ceil 
    count = []
    stack = []
    
    for progress, speed in zip(progresses, speeds):
        remain = ceil((100 - progress) / speed)

        if not count and not stack:
            stack.append(remain)
            count.append(1)
            continue
        
        if remain <= stack[-1]:
            count[-1]+=1
        else:
            stack.append(remain)
            count.append(1)
    
    answer = count
    return answer