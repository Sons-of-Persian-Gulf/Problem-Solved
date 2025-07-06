n, k = map(int, input().split())
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
password = ""
i = 0

while n != 0:
    password += arr[i]
    i += 1
    n -= 1
    if i == k:
        i = 0
print(password)
