import itertools

def is_prime(num):
    if num <= 1: return False
    for i in range(2, int(num ** 1/2)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    
    permuts = []
    for i in range(1,len(numbers)+1):
        data = itertools.permutations(numbers,i)
        permuts.extend([int(''.join(elem)) for elem in data])
    
    
    permuts = list(set(permuts))
    count = 0
    for permut in permuts:
        if is_prime(permut): count+=1
    return count