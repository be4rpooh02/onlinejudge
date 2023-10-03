def solution(s):
    answer = sum([int(num) if(num[-1]!="Z") else 0 for num in s.replace(" Z", "Z").split()])
    return answer