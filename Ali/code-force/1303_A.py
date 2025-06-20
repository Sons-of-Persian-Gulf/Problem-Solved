def min_zeros_to_erase(s: str) -> int:
    # Find first and last occurrence of '1'
    try:
        l = s.index('1')
        r = s.rindex('1')
    except ValueError:
        # No '1' in the string
        return 0
    # Count zeros between l and r
    return s[l:r+1].count('0')

# Read input and handle multiple test cases
t = int(input())
for _ in range(t):
    s = input().strip()
    print(min_zeros_to_erase(s))
