import sys
input = sys.stdin.readline

N = int(input())
candidates = [3, 5]
attempts = 1
valid_flag = True


def check_valid(arr):
    valid = False
    for data in arr:
        if data <= N:
            valid = True
    return valid


while True:
    valid = False
    found = False
    if not check_valid(candidates):
        valid_flag = False
        break
    temp = []
    for candidate in candidates:
        if candidate == N:
            found = True
            break
        temp.append(candidate+3)
        temp.append(candidate+5)
    if found == True:
        break
    attempts += 1
    candidates = list(set(temp))


print(attempts if valid_flag else -1)
