def solution(num_list):
    """
    # 풀이 1 (일반적인 함수)
    def num_divide(num):
        div=0
        while(num!=1):
            if(num%2):
                num-=1
            num, div = num/2, div+1
        return div
    
    answer = sum([num_divide(i) if(i!=1) else 0 for i in num_list])
    return answer
    """
    
    """
    # 풀이 2 (재귀함수)
    def num_divide(num, div):
        if(num==1):
            return div

        if(num%2):
            num-=1
            
        return num_divide(num/2, div+1)
    
    answer = sum([num_divide(i, 0) if(i!=1) else 0 for i in num_list])
    return answer
    """
    # 풀이 3 (Log2 함수 사용)
    import math
    
    answer = sum([int(math.log2(i)) if(i!=1) else 0 for i in num_list])
    return answer