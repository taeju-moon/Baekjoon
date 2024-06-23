def solution(s):
    stack = []
    
    for ho in s:
        if ho == "(":
            stack.append(ho)
        elif ho == ")":
            if (len(stack) == 0): return False
            stack.pop()
        
    

    return len(stack) == 0