datas_len = int(input())
datas = list(map(int, input().split(" ")))
should_sum = int(input())

arr = [0] * 2000001

for data in datas:
    arr[data] = 1

cnt = 0
for i in range(1, int((should_sum+1)/2), 1):
    if arr[i] == 1 and arr[should_sum-i] == 1 and i != should_sum - i: 
        cnt +=1

print(cnt)