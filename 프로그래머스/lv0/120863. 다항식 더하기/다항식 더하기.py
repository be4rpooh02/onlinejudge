def solution(polynomial):
    x, n = 0, 0
    for i in ("0 + "+polynomial).replace("+ x", "+ 1x").split(" + "):
        if("x" in i):
            x+=int(i[:-1])
        else:
            n+=int(i)
    
    if(n and x):
        answer = f"{x}x + {n}" if(x>1) else f"x + {n}"
    elif(n and not x):
        answer = f"{n}"
    elif(not n and x):
        answer = f"{x}x" if(x>1) else "x"
    else: 
        answer = ""

    return answer