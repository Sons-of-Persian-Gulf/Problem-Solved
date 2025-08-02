<<<<<<< HEAD
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
=======
for _ in range(int(input())):
    s = input()
    n = int(s)
    n = int(str(n)[::-1])
    print(str(n).count("0"))
        
>>>>>>> 8f3cdbd49cd1a281981b7a4b93b45c2cbb717c52
