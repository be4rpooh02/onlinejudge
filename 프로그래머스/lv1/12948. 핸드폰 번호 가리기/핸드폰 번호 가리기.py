def solution(phone_number):
    target_len = len(phone_number[:len(phone_number)-4])
    answer = '*'*target_len+phone_number[len(phone_number)-4:]
    return answer