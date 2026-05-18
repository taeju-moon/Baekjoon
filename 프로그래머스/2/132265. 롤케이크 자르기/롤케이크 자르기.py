def solution(topping):
    topping_size = len(topping)
    answer = 0
    right = {}
    
    for elem in topping:
        if elem not in right:
            right[elem] = 1
        else:
            right[elem] +=1
    
    left = {}
    
    for i in range(0, topping_size, 1):
        # 오른쪽에서 왼쪽으로 옮기기
        elem = topping[i]
        # 오른쪽에서 빼서
        right[elem] -=1
        if right[elem] == 0:
            del right[elem]
        # 왼쪽에 넣기
        if elem not in left:
            left[elem] = 1
        else:
            left[elem] +=1
        
        if len(right.keys()) == len(left.keys()):
            answer +=1
    return answer