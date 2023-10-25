def solution(n, wires):
    from collections import defaultdict, deque
    
    answer = n
    graph = defaultdict(set)
    isconn = [[True] * (n + 1) for _ in range(n+1)]
    
    def bfs(start, graph, visited, isconn):
        q = deque([start])
        visited[start] = True
        cnt = 1
        
        while q:
            now = q.popleft()
            
            for conn in graph[now]:
                if not visited[conn] and isconn[start][conn]:
                    q.append(conn)
                    visited[conn] = True
                    cnt += 1
                    
        return cnt

    for s, e in wires:
        graph[s].add(e)
        graph[e].add(s)
        
    for s, e in wires:
        visited = [False] * (n + 1)
        
        isconn[s][e] = False
        isconn[e][s] = False
        scnt = bfs(s, graph, visited, isconn)
        ecnt = bfs(e, graph, visited, isconn)
        isconn[s][e] = True
        isconn[e][s] = True
        
        answer = min(answer, abs(scnt - ecnt))
            
    return answer