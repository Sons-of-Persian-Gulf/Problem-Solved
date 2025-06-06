class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = dict()
        for i in stones:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        count = 0
        for i in jewels:
            if i in d:
                count += d[i]
        return count