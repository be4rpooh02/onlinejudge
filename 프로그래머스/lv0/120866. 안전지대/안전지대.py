def solution(board):
    l = len(board)
    done = set()
    for i in range(l):
        for j in range(l):
            if(board[i][j]):
                for m in range(max(i-1,0),min(i+2,l)):
                    for n in range(max(j-1,0),min(j+2,l)):
                        done.update([(m,n)])

    answer = len(board)**2 - len(done)
    return answer