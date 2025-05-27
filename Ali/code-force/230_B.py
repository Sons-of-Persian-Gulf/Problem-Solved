def get_primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

# 1. Generate primes up to 10^6
primes = get_primes_up_to(10**6)

# 2. Create set of T-primes (squares of primes)
t_primes = set(p * p for p in primes)

# 3. Read input and check
n = int(input())
numbers = list(map(int, input().split()))

for x in numbers:
    if x in t_primes:
        print("YES")
    else:
        print("NO")
