n = int(input())
s = input()
L = s.count("L")
R = n - L
print(abs(L + R) + 1)