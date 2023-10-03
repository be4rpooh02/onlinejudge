def solution(numbers):
    res= sorted(numbers)
    answer=max(res[0]*res[1], res[-1]*res[-2])
    #answer = max([i*j for idx,i in enumerate(numbers) for j in numbers[idx+1:]])
    return answer