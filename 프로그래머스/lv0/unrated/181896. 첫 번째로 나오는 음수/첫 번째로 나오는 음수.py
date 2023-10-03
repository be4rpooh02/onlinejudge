def solution(num_list):
    answer=-1
    for item in enumerate(num_list):
        if(item[1]<0):
            answer=item[0]
            break

    return answer