t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    odd_count = sum(1 for x in arr if x % 2 != 0)
    print("YES" if odd_count % 2 == 0 else "NO")
