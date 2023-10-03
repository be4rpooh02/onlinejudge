def solution(array):
    u = set(array)
    cnt = [array.count(num) for num in u]
    
    answer = sorted(zip(cnt,u))[-1][-1] if(cnt.count(max(cnt))==1) else -1
        
    return answer