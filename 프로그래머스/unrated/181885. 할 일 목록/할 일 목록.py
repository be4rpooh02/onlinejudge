def solution(todo_list, finished):
    answer = [item[0] for item in zip(todo_list, finished) if(not item[1])]
    return answer