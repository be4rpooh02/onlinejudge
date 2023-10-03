def solution(quiz):
    answer = ["O" if(eval(item.replace(" = ", " == "))) else "X" for item in quiz]
    
    return answer