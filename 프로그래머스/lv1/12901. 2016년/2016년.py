def solution(a, b):
    months = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    answer = days[(sum(months[:a])+b)%7-1]
    
    return answer