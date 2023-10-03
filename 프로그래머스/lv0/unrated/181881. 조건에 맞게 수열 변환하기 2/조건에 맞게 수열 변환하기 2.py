def solution(arr):
    prev, curr=[], arr.copy()
    answer=-1
    
    while(prev!=curr):
        answer+=1
        prev, curr=curr, []

        for num in prev:
            if(num%2 and not num//50):
                curr.append(num*2+1)
            elif(not num%2 and num//50):
                curr.append(num//2)
            else:
                curr.append(num)

    return answer