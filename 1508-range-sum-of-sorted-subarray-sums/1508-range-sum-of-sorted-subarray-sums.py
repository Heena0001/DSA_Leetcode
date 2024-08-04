class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result=[]
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s=s+nums[j]
                result.append(s)
        result.sort()
        mod = 10**9 + 7
        return sum(result[left - 1 : right]) % mod
                