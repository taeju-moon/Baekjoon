N = int(input())
datas = []
for i in range(N):
    datas.append(int(input()))

stack = []
for data in datas:
    if data == 0:
        stack.pop()
    else:
        stack.append(data)

print(sum(stack))