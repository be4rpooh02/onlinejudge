def solution(board, k):
    len_i=len(board)
    len_j=len(board[0])
    
    answer=sum(board[i][j] for i in range(len(board)) for j in range(len(board[i])) if(i+j<=k))
    return answer