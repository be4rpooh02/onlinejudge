def solution(str_list):
    num=-1
    answer=[]

    if "l" in set(str_list) or "r" in set(str_list):
        for idx, ch in enumerate(str_list):
            if ch in ["l", "r"]:
                num, res=(idx,ch)
                break
                    
        if(num > -1):
            answer=str_list[:num] if(res=="l") else str_list[num+1:]

    return answer