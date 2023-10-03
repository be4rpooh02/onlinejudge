def solution(arr):
    l_arr = len(arr)
    sqr = 0
    
    while(l_arr>(2**sqr)):
        sqr+=1
    
    answer = arr + [0]*(2**sqr-l_arr)
    return answer