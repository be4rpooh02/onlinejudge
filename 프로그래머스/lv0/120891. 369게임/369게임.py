def solution(order):
    nums=[3,6,9]
    answer = sum((int(num) in nums) for num in str(order))
    return answer