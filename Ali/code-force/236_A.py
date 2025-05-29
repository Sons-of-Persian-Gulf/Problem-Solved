s = input()

distinct_chars = set()
for i in s:
    distinct_chars.add(i)

print("CHAT WITH HER!" if len(distinct_chars) % 2 == 0 else "IGNORE HIM!")
