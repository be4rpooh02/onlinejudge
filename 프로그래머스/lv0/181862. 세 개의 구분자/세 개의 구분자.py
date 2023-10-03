def solution(myStr):
    res = myStr.replace("a", " ").replace("b", " ").replace("c", " ").strip().split()
    answer = res if(len(res)) else ["EMPTY"]
    return answer