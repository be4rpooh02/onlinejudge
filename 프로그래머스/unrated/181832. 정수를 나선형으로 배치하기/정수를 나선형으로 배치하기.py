def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]

    # move[0]: 우, move[1]: 하, move[2]: 좌, move[3]: 상
    move = [[0,1], [1,0],[0,-1],[-1,0]]
    # way: 0 = 우, 1 = 하, 2 = 좌, 3 = 상
    x,y,way = 0,0,0    

    for i in range(1, n**2+1):
        answer[y][x]=i
        # 범위를 벗어나는경우 (x or y) or 이미 방문한 경우
        if(y+move[way][0] >= n or x+move[way][1] >= n or answer[y+move[way][0]][x+move[way][1]]): 
            # 방향전환 (way): 0 = 우, 1 = 하, 2 = 좌, 3 = 상
            way = (way+1)%len(move)
        
        # 세로(y), 가로(x) 좌표 이동
        y,x = y+move[way][0], x+move[way][1]

    return answer

    