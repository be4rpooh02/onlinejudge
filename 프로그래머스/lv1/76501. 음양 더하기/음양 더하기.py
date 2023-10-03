def solution(absolutes, signs):
    answer = sum([num if(sign) else num*-1 for num, sign in zip(absolutes, signs)])
    return answer