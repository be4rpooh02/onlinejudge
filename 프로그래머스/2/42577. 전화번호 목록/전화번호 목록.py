def solution(phone_book):
    d = {}
    
    for phone in phone_book:
        d[phone] = len(phone)
        
    answer = True

    for key in d.keys():
        prefix = ""
        
        for ch in key:
            prefix+=ch
            
            if prefix in d and prefix != key:
                answer = False
                break

    return answer