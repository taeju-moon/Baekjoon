def solution(citations):
    n = len(citations)
    
    citations.sort(reverse=True)
    
    for i in range(1,n+1,1):
        if citations[i-1] < i:
            return i-1
    return n