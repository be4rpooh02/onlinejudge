def solution(lines):
    a, b, c = [set(range(min(l), max(l))) for l in lines]
    answer = len(a & b | b & c | c & a)
    return answer