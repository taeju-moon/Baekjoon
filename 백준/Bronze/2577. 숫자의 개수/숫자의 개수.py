a = int(input())
b = int(input())
c = int(input())
data = a * b * c

arr = [0] * 10
for s in str(data):
    arr[int(s)]+=1

for ar in arr:
    print(ar)