from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=cmp_to_key(cmp), reverse=True)
    return str(int(''.join(numbers)))


def cmp(a,b):
    return int(a+b) - int(b+a)
