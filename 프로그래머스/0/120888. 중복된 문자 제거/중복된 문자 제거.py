def solution(my_string):
    answer = ''
    for s in my_string:
        if not s in answer:
            answer = answer + s
    return answer