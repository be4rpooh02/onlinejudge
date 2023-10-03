// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120849

def solution(my_string):
    answer = ''.join([ch for ch in my_string if(ch not in ['a','e','i','o','u'])])
    return answer