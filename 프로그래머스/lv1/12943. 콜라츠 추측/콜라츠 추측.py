def solution(num):
    answer = -1
    cnt = 0
    while(cnt<500):
        if(num==1):
            answer = cnt
            break
        else:
            num = num*3+1 if(num%2) else num/2
            cnt+=1

    return answer