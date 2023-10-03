def solution(n, slicer, num_list):
    a,b,c = slicer[0], slicer[1], slicer[2]
    
    if(n%2):
        answer=num_list[a:b+1] if(n-1) else num_list[:b+1]
    else:
        answer=num_list[a:b+1:c] if(n-2) else num_list[a:]

    return answer