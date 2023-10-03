def solution(numbers):
    avg = 0

    for index in range(len(numbers)):
        avg = (avg*index+numbers[index])/(index+1)    

    answer = round(avg, 2)

    return answer