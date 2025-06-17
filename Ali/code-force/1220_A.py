from collections import Counter
n = int(input())
c = Counter(input())

# one
O = c["o"]
N = c["n"]
E = c["e"]
one_count = min(O, N, E)
c["o"] = O - one_count
c["n"] = N - one_count
c["e"] = E - one_count



# zero
Z = c["z"]
E = c["e"]
R = c["r"]
O = c["o"]
zero_count = min(Z, E, R, O)
ans = "1 " * one_count + "0 " * zero_count
print(ans.strip())



