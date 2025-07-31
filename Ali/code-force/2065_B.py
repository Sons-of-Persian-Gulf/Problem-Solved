import sys
input = sys.stdin.readline

def process(s: str) -> int:
    # Check for any pair of adjacent equal characters
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return 1
    return len(s)


t = int(input().strip())
for _ in range(t):
    s = input().strip()
    print(process(s))

