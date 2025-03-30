import math

def solution(progresses, speeds):
    answer = []
    stack = 0
    
    last_passed_time = 0
    for i in range(len(progresses)):
        left_mount = 100-progresses[i]
        passed_time = math.ceil(left_mount / speeds[i])
        if last_passed_time >= passed_time:
            stack+=1
        else:
            if (stack != 0): answer.append(stack)
            stack = 1
            last_passed_time = passed_time
    
    if (stack != 0): answer.append(stack)
    
    return answer