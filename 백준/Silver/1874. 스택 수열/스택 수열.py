N = int(input())
datas = []
for i in range(N):
    datas.append(int(input()))

stack = []
answer = []

def push(data):
    stack.append(data)
    answer.append("+")

def pop():
    answer.append("-")
    return stack.pop()

num = 1
data_to_find = datas.pop(0)

is_fail = False

while data_to_find and num <= N:
    if data_to_find >= num:
        push(num)
        num +=1
    elif data_to_find < num:
        if not stack:
            is_fail = True
            break
        top = pop()
        if top == data_to_find:
            if datas: data_to_find = datas.pop(0)
            else: data_to_find = None
        else:
            is_fail = True
            break
            

while stack and is_fail == False:
    top = stack.pop()
    if top == data_to_find:
        if datas: data_to_find = datas.pop(0)
        answer.append("-")
    else:
        is_fail = True
        break


if datas or is_fail:
    print("NO")
else:
    for ans in answer: print(ans)