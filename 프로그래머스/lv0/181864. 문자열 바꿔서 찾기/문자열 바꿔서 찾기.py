def solution(myString, pat):
    inv_pat = "".join(["B" if(ch=="A") else "A" for ch in pat])
    answer = 1 if(inv_pat in myString) else 0
    return answer