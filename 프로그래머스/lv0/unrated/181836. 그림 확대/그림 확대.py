def solution(picture, k):
    answer=[]
    for line in picture:
        row = ''.join([ch*k for ch in line])
        for i in range(k):
            answer.append(row)
    return answer