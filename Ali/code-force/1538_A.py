for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    max_pos = arr.index(max(arr)) + 1
    min_pos = arr.index(min(arr)) + 1
    # Option 1 - remove both from left
    option1 = max(min_pos, max_pos)

    # Option 2 - remove both from right
    option2 = max(n - max_pos + 1, n - min_pos + 1)

    # Option 3 - remove one from left and other from right
    option3 = min_pos + n - max_pos + 1

    # Option 4 - remove one from left and other from right
    option4 = max_pos + n - min_pos + 1

    print(min(option1, option2, option3, option4))

