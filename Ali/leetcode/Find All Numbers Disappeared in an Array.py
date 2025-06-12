class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        ans = []
        for i in range(1, len(nums) + 1):
            if i not in d:
                ans.append(i)
        return ans

