n = int(input())

edges = [[] for _ in range(n + 1)]

for i in range(1, n):
    x = int(input())
    edges[x].append(i + 1)

leafs = set()
# print(edges)
for i in range(1, n + 1):
    if not edges[i]:
        leafs.add(i)
# print(leafs)
flag = True


def has_three_leaf_at_least(node):
    cnt = 0
    for e in edges[node]:
        if e in leafs:
            cnt += 1
    return cnt >= 3


for i in range(1, n):
    if edges[i]:
        if not has_three_leaf_at_least(i):
            flag = False
            break

if flag:
    print("Yes")
else:
    print("No")