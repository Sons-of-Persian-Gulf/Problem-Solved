def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisibility by numbers of form 6k ± 1 up to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


n, m = map(int, input().split())

# Find the next prime after n
next_prime = n + 1
while not is_prime(next_prime):
    next_prime += 1

print("YES" if next_prime == m else "NO")


