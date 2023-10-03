def solution(myString):
    answer=''.join([ "l" if(ch in "abcdefghijk") else ch for ch in myString])
    return answer