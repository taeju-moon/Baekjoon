data = [
    "G...", ".I.T", "..S."
]

K = int(input())

for line in data:
    for i in range(K):
        for s in line:
            print(s * K, end="")
        print()
