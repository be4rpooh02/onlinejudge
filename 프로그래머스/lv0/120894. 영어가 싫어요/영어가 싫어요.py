def solution(numbers):
    chs = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for idx, ch in enumerate(chs):
        numbers = numbers.replace(ch, str(idx))

    answer = int(numbers)
    return answer