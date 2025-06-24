def max_pyramid_height(n: int) -> int:
    levels = 0       # Number of complete levels built
    current_sum = 0  # Sum of cubes required for the next level

    while True:
        levels += 1
        current_sum += levels  # We need `levels` more cubes for this level
        if current_sum > n:
            return levels - 1
        n -= current_sum         # Deduct cubes used so far

# Read input and output the result
n = int(input().strip())
print(max_pyramid_height(n))
