def solution(order):
    res = " ".join(order).replace("ice", "").replace("hot", "").split().count("cafelatte")
    answer = 4500*len(order) + 500*res
    return answer