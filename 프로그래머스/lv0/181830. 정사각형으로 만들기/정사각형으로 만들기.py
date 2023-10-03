def solution(arr):
    rows, cols=len(arr), len(arr[0])
    if(rows>cols):
        answer=[row + [0]*(rows-cols) for row in arr]
    elif(rows<cols):
        answer=arr + [[0]*cols]*(cols-rows)
    else:
        answer=arr

    return answer