# for _ in range(int(input())):
#     n = int(input())
#     edges = [[] for _ in range(n)]
#     arr = input()
#
#     for i in range(n):
#         if arr[i] == "-":
#             edges[i].append((i + 1) % n)
#             edges[(i + 1) % n].append(i)
#         elif arr[i] == ">":
#             edges[i].append((i + 1) % n)
#         elif arr[i] == "<":
#             edges[(i + 1) % n].append(i)
#     # print(edges)
#     # cnt = 0
#     # for i in range(n):
#     #     if len(edges[i]) >= 1:
#     #         x = i
#     #         for j in edges[i]:
#     #             if i in edges[j]:
#     #                 cnt += 1
#     #                 break
#     def dfs(node):
#         visited = [False] * n
#         visited[node] = False
#         x = node
#         stack = [node]
#         while stack:
#             node = stack.pop()
#             for neighbor in edges[node]:
#                 if neighbor == x:
#                     return True
#                 if not visited[neighbor]:
#                     stack.append(neighbor)
#         return False
#
#     cnt = 0
#
#     for i in range(n):
#         if arr[i] == "-":
#             cnt += 1
#             continue
#         result = dfs(i)
#         if result:
#             cnt += 1
#
#     print(cnt)
for _ in range(int(input())):
    n = int(input())
    s = input()

    # Check if all arrows point one way
    all_right = all(c != '<' for c in s)
    all_left = all(c != '>' for c in s)

    if all_right or all_left:
        print(n)
        continue

    cnt = 0
    for i in range(n):
        if s[i] == '-' or s[(i - 1) % n] == '-':
            cnt += 1

    print(cnt)

