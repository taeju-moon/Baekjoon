def solution(arr):
    answer = []
    for data in arr:
        if (len(answer) > 0 ):
            if (answer[-1] != data):
                answer.append(data)
        else:
            answer.append(data)
    return answer