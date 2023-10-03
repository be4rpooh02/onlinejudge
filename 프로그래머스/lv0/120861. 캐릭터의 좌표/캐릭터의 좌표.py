def solution(keyinput, board):
    x,y = 0,0
    maxx, maxy = (board[0]-1)/2, (board[1]-1)/2
    
    for i in keyinput:
        if(i=="right"):
            x=x+1 if(x<maxx) else x
        elif(i=="left"):
            x=x-1 if(x>maxx*-1) else x
        elif(i=="up"):
            y=y+1 if(y<maxy) else y
        else:
            y=y-1 if(y>maxy*-1) else y
            
    answer = [x,y]
    return answer
