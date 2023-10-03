def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1] if(num2>0) else []
    return answer