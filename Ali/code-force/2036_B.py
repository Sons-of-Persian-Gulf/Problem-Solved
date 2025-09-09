import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    brand_cost = {}

    for _ in range(k):
        b, c = map(int, input().split())
        brand_cost[b] = brand_cost.get(b, 0) + c

    # Get the values (total cost per brand), sort descending
    sorted_costs = sorted(brand_cost.values(), reverse=True)

    # Sum the top n costs (or all if less than n)
    ans = sum(sorted_costs[:n])
    print(ans)
