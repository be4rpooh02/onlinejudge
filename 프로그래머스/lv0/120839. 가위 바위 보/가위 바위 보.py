def solution(rsp):
    pat={"2":"0", "0":"5", "5":"2"}
    answer = ''.join([pat[ch] for ch in rsp])
    return answer