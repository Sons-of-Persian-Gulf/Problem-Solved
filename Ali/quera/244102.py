# police = int(input())
# thief = int(input())
#
# edges = [[], [2, 3, 4], [1, 3, 4, 5, 6], [1, 2, 4, 6, 7], [1, 2, 3, 5, 6, 7], [2, 4, 6], [2, 3, 4, 5, 7], [3, 4, 6]]
#
#
# police_moves = set(i for i in edges[police])
# thief_moves = set(i for i in edges[thief])
# police_moves.add(police)
# thief_moves.add(thief)
# # a = {1, 2, 3, 4, 5, 6, 7}
# # print(police_moves)
# # print(thief_moves)
# # x = thief_moves.difference(police_moves)
# # print(x)
# print()
# if len(thief_moves.difference(police_moves)) == 0 or thief in police_moves:
#     print(1)
# else:
#     print(2)
#
#
from collections import deque

police = int(input())
thief = int(input())

edges = [[],
         [2, 3, 4],
         [1, 3, 4, 5, 6],
         [1, 2, 4, 6, 7],
         [1, 2, 3, 5, 6, 7],
         [2, 4, 6],
         [2, 3, 4, 5, 7],
         [3, 4, 6]
]

# state: (police_pos, thief_pos, turn, days_passed)
# turn = 0 (police), 1 (thief)
queue = deque()
visited = set()

queue.append((police, thief, 0, 0))
visited.add((police, thief, 0))

while queue:
    p, t, turn, days = queue.popleft()

    if p == t:
        print(days)
        break

    if turn == 0:  # police's turn
        for np in edges[p]:
            if (np, t, 1) not in visited:
                visited.add((np, t, 1))
                queue.append((np, t, 1, days))  # same day
    else:  # thief's turn
        for nt in edges[t]:
            if (p, nt, 0) not in visited:
                visited.add((p, nt, 0))
                queue.append((p, nt, 0, days + 1))  # next day
else:
    print(-1)

