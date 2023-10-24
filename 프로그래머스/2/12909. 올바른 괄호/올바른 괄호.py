def solution(s):
    stack = []
    
    if not s:
        return True
    
    if s[0] == ")":
        return False
    
    for ch in s:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if stack:
                stack.pop()
            else:
                return False
        else:
            continue
    
    answer = True if not stack else False

    return answer