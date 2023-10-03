def solution(A, B):
    """
    answer = -1
    for i, _ in enumerate(A):
        if(A[len(A)-i:]+A[:len(A)-i] ==B):
            answer = i
            break
    """
    answer = (B*2).find(A)

    return answer