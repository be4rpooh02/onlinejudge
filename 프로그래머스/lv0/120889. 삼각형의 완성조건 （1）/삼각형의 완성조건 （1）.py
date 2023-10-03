def solution(sides):
    m = max(sides)
    answer = (sum(sides)-m <= m)+1
    return answer