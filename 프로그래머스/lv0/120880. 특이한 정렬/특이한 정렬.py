def solution(numlist, n):
    # answer = [-x for _,x in sorted([(abs(num-n), -num) for num in numlist])]
    answer = sorted(numlist, key=(lambda x: (abs(x-n), -x)))
    
    return answer