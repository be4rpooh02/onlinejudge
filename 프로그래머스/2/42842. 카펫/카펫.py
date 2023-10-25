def solution(brown, yellow):
    total = brown + yellow
    end = int(total ** 0.5) + 1
    answer = []
    
    for y in range(3, end):
        if not total % y:
            ix = (total // y) - 2
            iy = y - 2
            
            if ix * iy == yellow:
                answer = [total//y, y]

    return answer