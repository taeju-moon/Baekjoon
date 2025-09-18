from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
rings = {

}

for _ in range(N):
    name, ring = input().split()
    if ring == "-":
        continue
    if rings.get(ring):
        rings[ring].append(name)
    else:
        rings[ring] = [name]


cases = []
for ring in rings.keys():
    if len(rings[ring]) == 2:
        for combi in combinations(rings[ring], 2):
            cases.append(combi)

print(len(cases))
for case in cases:
    print(case[0], case[1])
