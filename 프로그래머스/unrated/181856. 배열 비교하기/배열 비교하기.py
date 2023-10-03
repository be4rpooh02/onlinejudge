def solution(arr1, arr2):
    l_arr1, l_arr2 = len(arr1), len(arr2)

    answer=1 if(l_arr1 > l_arr2) else -1
    
    if(l_arr1 == l_arr2):
        s_arr1, s_arr2 = sum(arr1), sum(arr2)
        answer=1 if(s_arr1>s_arr2) else (-1 if(s_arr1 < s_arr2) else 0)

    return answer