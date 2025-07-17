for _ in range(int(input())):
    d = dict()
    letters = input()
    word = input()
    for i in range(26):
        d[letters[i]] = i + 1
    cnt = 0
    
    for i in range(1, len(word)):
        cnt += abs(d[word[i]] - d[word[i - 1]])
    print(cnt)
    # print("")
    # print("---------------------------")