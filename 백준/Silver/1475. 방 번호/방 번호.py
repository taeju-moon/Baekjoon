data = input()

cnt = 1
numbers = {
    '0': 1,
    "1": 1,
    "2": 1,
    "3":1,
    "4":1,
    "5":1,
    "6-9":2,
    "7": 1,
    "8":1,
}

def get_one_more_set():
    global numbers
    global cnt
    for num in numbers:
        if num == "6-9":
            numbers[num] +=2
        else:
            numbers[num] +=1
    cnt +=1

for num in data:
    if num == '6' or num == '9':
        if numbers['6-9'] == 0:
            get_one_more_set()
            numbers["6-9"] -=1
        else:
            numbers["6-9"] -=1
    else:
        if numbers[num] == 0:
            get_one_more_set()
            numbers[num] -=1
        else:
            numbers[num] -=1

print(cnt)