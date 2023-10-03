def solution(date1, date2):
    d1=int(''.join([str(item) for item in date1]))
    d2=int(''.join(str(item) for item in date2))
          
    answer = 1 if(d1 < d2) else 0
    return answer