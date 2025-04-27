def solution(citations):
    #1. 내림차순 정렬
    citations.sort(reverse=True)
    
    for index, data in enumerate(citations):
        if index +1 > data:
            return index
    return len(citations)