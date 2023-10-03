def solution(id_pw, db):
    answer = "fail"
    
    for info in db:
        if(id_pw[0] == info[0]):
            if(id_pw[1] == info[1]):
                answer = "login"
            else:
                answer = "wrong pw"
            break

    return answer