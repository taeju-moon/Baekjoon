import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    success = True
    while True:
        if scoville[0] >= K:
            break
        if len(scoville) < 2:
            success = False
            break
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        mixed = first + second * 2
        heapq.heappush(scoville, mixed)
        answer +=1
        
    if success:
        return answer
    else:
        return -1