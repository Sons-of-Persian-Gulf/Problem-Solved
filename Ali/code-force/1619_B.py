import math

def count_liked_numbers(n):
    squares = math.isqrt(n)
    
    # Cube root using integer arithmetic
    cubes = int(n ** (1/3))
    while (cubes + 1) ** 3 <= n:
        cubes += 1
    while cubes ** 3 > n:
        cubes -= 1

    # Sixth root using integer arithmetic
    sixth_powers = int(n ** (1/6))
    while (sixth_powers + 1) ** 6 <= n:
        sixth_powers += 1
    while sixth_powers ** 6 > n:
        sixth_powers -= 1

    return squares + cubes - sixth_powers

# Input
t = int(input())
for _ in range(t):
    n = int(input())
    print(count_liked_numbers(n))
