// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120824

def solution(num_list):
    length = len(num_list)
    odd = sum(map(lambda x: x%2, num_list))

    answer = [length-odd, odd]
    return answer