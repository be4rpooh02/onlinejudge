def solution(s, n):
    answer = ""
    
    for ch in s:
        if(ch == " "):
            answer+=ch
        elif(ch.isupper()):
            answer += chr(ord("A")+(ord(ch)-ord("A")+n)%26)
        else:
            answer += chr(ord("a")+(ord(ch)-ord("a")+n)%26)
    
    return answer