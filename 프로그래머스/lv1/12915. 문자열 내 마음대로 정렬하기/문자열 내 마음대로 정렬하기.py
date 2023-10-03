def solution(strings, n):
    answer = sorted(strings, key=lambda s: [s[n], s])
    
    # answer = [t for ch, t in sorted((s[n],s) for s in strings)]
    
    return answer