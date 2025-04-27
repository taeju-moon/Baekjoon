import itertools


def solution(k, dungeons):
    answer = 0
    
    permuts = [list(data) for data in itertools.permutations(dungeons)]
    
    #모든 경우의 수 알아보기
    for permut in permuts:
        cnt = 0
        using_k = k
        for dungeon in permut:
            if dungeon[0] > using_k: continue
            if dungeon[1] <= using_k:
                using_k -= dungeon[1]
                cnt +=1
        if cnt >= answer: answer = cnt
    return answer