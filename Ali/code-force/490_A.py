n = int(input())
skills = list(map(int, input().split()))

# Store indices (1-based) of each type
programmers = []
mathematicians = []
pe_students = []


for i in range(n):
    if skills[i] == 1:
        programmers.append(i + 1)
    elif skills[i] == 2:
        mathematicians.append(i + 1)
    else:
        pe_students.append(i + 1)

print(min(len(programmers), len(mathematicians), len(pe_students)))
while programmers and mathematicians and pe_students:
    print(programmers.pop(), mathematicians.pop(), pe_students.pop())

