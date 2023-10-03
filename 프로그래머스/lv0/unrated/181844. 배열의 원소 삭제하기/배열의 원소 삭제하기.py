def solution(arr, delete_list):
    for item in arr:
        answer = [ item for item in arr if(item not in delete_list) ]
    return answer