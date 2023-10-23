def solution(genres, plays):
    import heapq

    answer = []
    plist = {}    # music list
    tp = {}    # total play
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        tp[genre] = play if not tp.get(genre) else tp[genre] + play
        
        if not plist.get(genre):
            plist[genre] = []
        
        heapq.heappush(plist[genre], (-play, idx))
        
    tp = sorted(tp.items(), key=lambda x: x[-1], reverse=True)

    for genre, gc in tp:
        for _ in range(2):
            if not plist[genre]:
                break
            answer.append(heapq.heappop(plist[genre])[-1])
    
    return answer