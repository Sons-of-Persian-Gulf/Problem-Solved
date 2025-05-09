n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n - 1):
    x = arr[i - 1] % 2
    y = arr[i] % 2
    z = arr[i + 1] % 2

    if x == y and y == z:
        continue
    else:
        if x == y:
            print(i + 1 + 1)
        elif x == z:
            print(i + 1)
        elif y == z:
            print(i - 1 + 1)
        break

# n = int(input())
# arr = list(map(int, input().split()))
#
# # Step 1: Check first 3 numbers to determine majority parity
# first_three = arr[:3]
# parities = [x % 2 for x in first_three]
#
# # Majority is 0 (even) or 1 (odd)
# majority_parity = 0 if parities.count(0) > 1 else 1
#
# # Step 2: Find and print the index of the number with minority parity
# for i in range(n):
#     if arr[i] % 2 != majority_parity:
#         print(i + 1)  # Output 1-based index
#         break
