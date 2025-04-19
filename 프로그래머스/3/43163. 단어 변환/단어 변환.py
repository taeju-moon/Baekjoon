def CanBeNext(a,b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]: diff +=1
    return diff <= 1

def solution(begin, target, words):
    answer = 0
    queue = []
    visited = [0] * len(words)
    
    if begin == target: return 0
    
    for index, word in enumerate(words):
        if CanBeNext(begin,word):
            queue.append([ word, index, 1 ])
            visited[index] = True
            
    while queue:
        word, index, count = queue.pop(0)
        if word == target:
            return count
        for id,wd in enumerate(words):
            if not visited[id] and CanBeNext(word,wd):
                queue.append([wd, id, count+1])
                visited[id] = True
            
    return 0