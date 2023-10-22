def solution(phone_book):
    d = {}
    answer = True
    
    for phone in phone_book:
        d[phone] = 1

    for key in d.keys():
        prefix = ""
        
        for ch in key:
            prefix += ch 

            if prefix in d and prefix != key:
                answer = False
                break
                
        if not answer:
            break
        
    return answer